#!/usr/bin/env python

__author__ = 'ariannagbasha, collabs: Shanquel and Sondos'

import requests
import turtle
import urllib.request
import json
import time


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
    return [lon, lat]


def graphics():
    ls = cooridnates()
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')
    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)
    iss.penup()
    iss.goto(float(ls[0]), float(ls[1]))


def indiana_time():
    lat_indy = 39.76838
    lon_indy = -86.15804
    location_indy = turtle.Turtle()
    location_indy.penup()
    location_indy.color('yellow')
    location_indy.goto(lon_indy, lat_indy)
    location_indy.dot(5)
    location_indy.hideturtle()
    url = 'http://api.open-notify.org/iss-pass.json?'
    params = f'lat={lat_indy}&lon={lon_indy}'
    response_indy = urllib.request.urlopen(url + params)
    result_indy = json.loads(response_indy.read())
    over_indy = result_indy['response'][1]['risetime']
    location_indy.write(time.ctime(over_indy), font=('Roboto', 10, 'bold'))


def main():
    astronauts()
    cooridnates()
    graphics()
    indiana_time()
    turtle.done()


if __name__ == '__main__':
    main()
