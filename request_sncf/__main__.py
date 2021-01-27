import logging
from gares import MyGares
from routes import MyRoutes

logging.basicConfig(level=logging.DEBUG,
                    filename="LOG_main_sncf.log",
                    filemode="a", #append ou W pour écraser
                    format='%(asctime)s : %(levelname)s : %(message)s')


def main():
    logging.info("init __main__.py")


    Gares = MyGares()
    while Gares.pages < 5 :
        Gares.fgares_finder(Gares.fgares_request())
    Gares.fgares_storage() 


    Routes = MyRoutes()
    Routes.froutes_finder(Routes.froutes_read(Routes.froutes_request()))
    Routes.froutes_storage()


if __name__=='__main__':
    main()