def main():
    open("/Users/adri/Downloads/Pruebas semana 1/Módulo 10/open.py")

if __name__ == '__main__':
    main()

python3 open.py
Traceback (most recent call last):
  File "/tmp/open.py", line 5, in <module>
    main()
  File "/tmp/open.py", line 2, in main
    open("/path/to/mars.jpg")
FileNotFoundError: [Errno 2] No such file or directory: '/Users/adri/Downloads/Pruebas semana 1/Módulo 10/open.py'