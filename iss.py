#!/usr/bin/env python

__author__ = 'ariannagbasha, collabs: Shanquel and Sondos'

import requests
import turtle


def astronauts():
    r = requests.get('http://api.open-notify.org/astros.json').json()
    num_peeps = r['number']
    for astros in r['people']:
        print(['name'])
    print(f'Number of people in the station: {num_peeps}')


def cooridnates():
    r = requests.get('http://api.open-notify.org/iss-now.json').json()
    lat = r['iss_position']['latitude']
    lon = r['iss_position']['longitude']
    print(f'Iss Position: {lat} {lon}')
    postion = lat and lon
    return postion


def graphics():
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')
    screen.register_shape('iss.gif')

def find


def main():
    astronauts()
    cooridnates()
    graphics()


if __name__ == '__main__':
    main()
