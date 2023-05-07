from src import utils

def main():

    x,y, height = utils.get_meta('data/images/DJI_0902-2022-03-23-10-58-32.jpg')
    print(x, y, height)

if __name__ == '__main__':
    main()