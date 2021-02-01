import logging
from endpoints import MyEndpoints
from gares import MyGares
from routes import MyRoutes

logging.basicConfig(level=logging.DEBUG,
                    filename="LOG_main_sncf.log",
                    filemode="a", #append ou W pour écraser
                    format='%(asctime)s : %(levelname)s : %(message)s')


def main():
    logging.info("init __main__.py")

    try:
        MyEP = MyEndpoints()
        MyEP.fep_finder(MyEP.fep_write(MyEP.fep_request()))
        MyEP.fep_storage()
        logging.info("endpoint request success")
    
    except:
        logging.warning("Failure endpoint request")


    try:
        Gares = MyGares()
        while Gares.pages <= 5 :
            Gares.fgares_finder(Gares.fgares_write(Gares.fgares_request()))
            Gares.pages += 1
        Gares.fgares_storage() 
        logging.info('gares areas request success')
    except:
        logging.warning('Failure gares areas request')
        

    try:
        Routes = MyRoutes()
        Routes.froutes_finder(Routes.froutes_write(Routes.froutes_request()))
        Routes.froutes_storage()
    except:
        logging.warning('Failure routes request')


if __name__=='__main__':
    main()