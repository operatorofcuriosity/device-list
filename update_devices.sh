#!/bin/sh

echo "<html><body><h1>裝置清單</h1><ul>" > /www/devices.html

cat /proc/net/arp | tail -n +2 | while read ip type flags mac mask iface; do
  echo "<li>$ip - $mac</li>" >> /www/devices.html
done

echo "</ul></body></html>" >> /www/devices.html
