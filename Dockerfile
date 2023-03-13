FROM osgeo/gdal:ubuntu-full-3.6.3

COPY data /data
COPY test.py /test.py

CMD [ "python", "-m", "test", "-h" ]
