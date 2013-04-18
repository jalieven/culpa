#!/usr/bin/python
print "Content-Type: text/html\n\n"

import cgi
import os
import sys

sys.stderr = sys.stdout

__version__ = '1.0a'
UUID = os.system('cat /proc/sys/kernel/random/uuid')


def s_speak(text):
    cmd = 'dbus-send --system --dest=com.mindscape.karotz.Voice /com/mindscape/karotz/Voice com.mindscape.karotz.KarotzInterface.tts_speak string:' + str(
        UUID) + ' string:"' + text + '" string:en int32:1'
    os.system(cmd)
    return 'Bunny says: ' + text


def s_shineled(color):
    os.system('killall led > /dev/null')
    cmd = 'dbus-send --system --dest=com.mindscape.karotz.Led /com/mindscape/karotz/Led com.mindscape.karotz.KarotzInterface.light string:' + str(
        UUID) + ' string:' + color
    os.system(cmd)
    return 'Shining LED with color:' + color


def s_fadeled(color, period):
    os.system('killall led > /dev/null')
    cmd = 'dbus-send --system --dest=com.mindscape.karotz.Led /com/mindscape/karotz/Led com.mindscape.karotz.KarotzInterface.fade string:' + str(
        UUID) + ' string:' + color + ' int32:' + period
    os.system(cmd)
    return 'Fading LED to color:' + color + ' in period:' + period + 'ms'


def s_pulseled(fromcolor, tocolor, period, length):
    os.system('killall led > /dev/null')
    cmd = 'dbus-send --system --dest=com.mindscape.karotz.Led /com/mindscape/karotz/Led com.mindscape.karotz.KarotzInterface.pulse string:' + str(
        UUID) + ' string:' + fromcolor + ' string:' + tocolor + ' int32:' + period + ' int32:' + length
    os.system(cmd)
    return 'Pulsing LED from color:' + fromcolor + ' to color:' + tocolor + ' with period:' + period + 'ms and length:' + length + 'ms'


def s_earflap(ear, step, speed):
    if ear == 'right':
        cmd = 'dbus-send --system --dest=com.mindscape.karotz.Ears /com/mindscape/karotz/Ears com.mindscape.karotz.KarotzInterface.move_right_step string:' + str(
            UUID) + ' int32:' + step + ' int32:' + speed
    elif ear == 'left':
        cmd = 'dbus-send --system --dest=com.mindscape.karotz.Ears /com/mindscape/karotz/Ears com.mindscape.karotz.KarotzInterface.move_left_step string:' + str(
            UUID) + ' int32:' + step + ' int32:' + speed
    os.system(cmd)
    return 'Ear:' + ear + ' flapped to step:' + step + ' with speed:' + speed


def s_earsflap(stepright, speedright, stepleft, speedleft):
    cmd = 'dbus-send --system --dest=com.mindscape.karotz.Ears /com/mindscape/karotz/Ears com.mindscape.karotz.KarotzInterface.move_step string:' + str(
        UUID) + ' int32:' + stepleft + ' int32:' + speedleft + ' int32:' + stepright + ' int32:' + speedright
    os.system(cmd)
    return 'Flapped right ear to step:' + stepright + ' with speed:' + speedright + ' and left ear to step:' + stepleft + ' with speed:' + speedleft


def s_earsreset():
    cmd = 'dbus-send --system --dest=com.mindscape.karotz.Ears /com/mindscape/karotz/Ears com.mindscape.karotz.KarotzInterface.reset string:' + str(
        UUID) + ' string:reset'
    os.system(cmd)
    return 'Ears reset.'


def s_playmedia(mediaurl):
    cmd = 'dbus-send --system --dest=com.mindscape.karotz.Multimedia /com/mindscape/karotz/Multimedia com.mindscape.karotz.KarotzInterface.play string:' + str(
        UUID) + ' string:' + mediaurl + ' int32:1'
    os.system(cmd)
    return 'Playing media:' + mediaurl


def main():
    form = cgi.FieldStorage()

    cmd = cgi.escape(form.getvalue('cmd', 'earsreset'))
    color = cgi.escape(form.getvalue('color', ''))
    period = cgi.escape(form.getvalue('period', ''))
    length = cgi.escape(form.getvalue('length', ''))
    text = cgi.escape(form.getvalue('text', ''))
    fromcolor = cgi.escape(form.getvalue('fromcolor', ''))
    tocolor = cgi.escape(form.getvalue('tocolor', ''))
    step = cgi.escape(form.getvalue('step', ''))
    stepright = cgi.escape(form.getvalue('stepright', ''))
    stepleft = cgi.escape(form.getvalue('stepleft', ''))
    speed = cgi.escape(form.getvalue('speed', ''))
    speedright = cgi.escape(form.getvalue('speedright', ''))
    speedleft = cgi.escape(form.getvalue('speedleft', ''))
    mediaurl = cgi.escape(form.getvalue('mediaurl', ''))

    res = 'Cannot comply!'
    if cmd == 'speak': res = s_speak(text)
    if cmd == 'shineled': res = s_shineled(color)
    if cmd == 'fadeled': res = s_fadeled(color, period)
    if cmd == 'pulseled': res = s_pulseled(fromcolor, tocolor, period, length)
    if cmd == 'leftflap': res = s_earflap('left', step, speed)
    if cmd == 'rightflap': res = s_earflap('right', step, speed)
    if cmd == 'earsflap': res = s_earsflap(stepright, speedright, stepleft, speedleft)
    if cmd == 'earsreset': res = s_earsreset()
    if cmd == 'playmedia': res = s_playmedia(mediaurl)

    print res


if __name__ == '__main__': main()