#!/usr/bin/env python
"""Basic usage example and testing of pysma."""
import argparse
import asyncio
import logging
import signal
import sys
import json
import aiohttp

import pysmaplus as pysma

# This example will work with Python 3.9+

_LOGGER = logging.getLogger(__name__)

VAR = {}


def print_table(sensors):
    """Print sensors formatted as table."""
    if (len(sensors) == 0):
        print("No Sensors found!")
    for sen in sensors:
        if sen.value is None:
            print("{:>25}".format(sen.name))
        elif sen.name is None:
            print("{:>25}{:>15} {} {}".format(sen.key, str(sen.value), sen.unit if sen.unit else "", sen.mapped_value if sen.mapped_value else "" ))
        else:
            print("{:>25}{:>15} {} {}".format(sen.name, str(sen.value), sen.unit if sen.unit else "", sen.mapped_value if sen.mapped_value else "" ))


async def identify(url: str, savedebug: bool):
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        ret = await pysma.autoDetect(session, url)
        print("{:>15}{:>10}    {}".format("Access", "", "Remarks"))
        for r in ret:
               print("{:>15}{:>10}    {}".format(r["access"], r["status"], (r["remark"] + " " +  r["device"]).strip()))
        if savedebug:
            f = open("example.log", "w")
            f.write(json.dumps(ret ,default=lambda o: str(o), indent=4))


async def main_loop(user: str, password, url: str, accessmethod: str, delay: float, cnt: int, savedebug: bool, isVerbose: bool):
    """Run main loop."""
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        _LOGGER.debug(f"MainLoop called! Url: {url} User/Group: {user} Accessmethod: {accessmethod}")
        VAR["sma"] = pysma.getDevice(session, url, password, user, accessmethod)
        try:
            await VAR["sma"].new_session()
        except pysma.exceptions.SmaAuthenticationException:
            _LOGGER.warning("Authentication failed!")
            return
        except pysma.exceptions.SmaConnectionException:
            _LOGGER.warning("Unable to connect to device at %s", url)
            return

        # We should not get any exceptions, but if we do we will close the session.
        try:
            VAR["running"] = True
            device_info = await VAR["sma"].device_info()
            sensors = await VAR["sma"].get_sensors()
            for name, value in device_info.items():
               print("{:>15}{:>25}".format(name, value))
            print("=====================================================================================")

            # enable all sensors
            for sensor in sensors:
                sensor.enabled = True

            while VAR.get("running"):
                await VAR["sma"].read(sensors)
                print_table(sensors)
                cnt -= 1
                if cnt == 0:
                    break
                await asyncio.sleep(delay)
                print("=====================================================================================")
        finally:
            _LOGGER.info("Closing Session...")
            dump = json.dumps(await VAR["sma"].get_debug(), indent=4)
            if isVerbose:
                
                print(dump)
            if savedebug:
                f = open("example.log", "w")
                f.write(dump)
            await VAR["sma"].close_session()

def getVersion():
    versionstring = "unknown"
    from importlib.metadata import version, PackageNotFoundError
    try:
        versionstring = version('pysma-plus')
    except PackageNotFoundError:
        pass
    return versionstring


async def main():
    print("Library version: " + getVersion())
    parser = argparse.ArgumentParser(prog='python example.py',
                                     description="Test the pysma library.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--verbose', action='store_true', help = "Enable debug output") 
    parser.add_argument('-d', '--delay', type=float, default=2, help = "Delay between two requests [seconds]")
    parser.add_argument('-c', '--count', type=int, default=1, help = "Number of requests (0=unlimited)")
    parser.add_argument('-s', '--save', action='store_true', help = "Save debug information to example.log")

    subparsers = parser.add_subparsers(help='Supported devices', required=True)

    parser_a = subparsers.add_parser('webconnect', help='Devices with Webconnect interface')
    parser_a.add_argument("user", choices=["user", "installer"], help="Login username")
    parser_a.add_argument("password", help="Login password")
    parser_a.add_argument('url', type=str, help='Url or IP-Address')
    parser_a.set_defaults(accessmethod="webconnect")

    parser_b = subparsers.add_parser('speedwire', help='Devices with Speedwire interface (unencrypted only)')
    parser_b.add_argument("user", choices=["user", "installer"], help="Login username")
    parser_b.add_argument("password", help="Login password")
    parser_b.add_argument('url', type=str, help='Url or IP-Address')
    parser_b.set_defaults(accessmethod="speedwireinv")

    parser_c = subparsers.add_parser('ennexos', help='EnnexOs based Devices')
    parser_c.set_defaults(accessmethod="ennexos")
    parser_c.add_argument("user", help="Username")
    parser_c.add_argument("password", help="Login password")
    parser_c.add_argument('url', type=str, help='Hostname or IP-Address')

    parser_d = subparsers.add_parser('energymeter', help='Energy Meters')
    parser_d.set_defaults(user="")
    parser_d.set_defaults(password="")
    parser_d.set_defaults(url="")
    parser_d.set_defaults(accessmethod="speedwireem")

    parser_e = subparsers.add_parser('identify', help='Tries to identify the available interfaces')
    parser_e.set_defaults(user="")
    parser_e.set_defaults(password="")
    parser_e.add_argument('url', type=str, help='Hostname or IP-Address')
    parser_e.set_defaults(accessmethod="identify")


    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    if args.verbose:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


    if args.accessmethod == "identify":
        print("Identification can take up to 30 seconds...\n")
        if not args.verbose:
            logging.basicConfig(stream=sys.stdout, level=logging.FATAL)
        await identify(args.url, args.save)
    else:
        def _shutdown(*_):
            VAR["running"] = False
        signal.signal(signal.SIGINT, _shutdown)
        await main_loop(user=args.user, password=args.password, url=args.url, accessmethod=args.accessmethod,
                        delay=args.delay, cnt=args.count, savedebug = args.save, isVerbose = args.verbose)


if __name__ == "__main__":
    asyncio.run(main())
