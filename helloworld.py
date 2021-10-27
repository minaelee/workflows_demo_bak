import sys


def main():
    print("Hello World!" + str(sys.version_info))
    if sys.version_info >= (3, 6) and sys.version_info < (3, 7):
        raise Exception("This app is not compatible with Python 3.6.")
        
        
if __name__ == "__main__":
    main()
