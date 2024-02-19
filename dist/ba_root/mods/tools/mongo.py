from pymongo import MongoClient
from efro.terminal import Clr
import setting
settings = setting.get_settings_data()
mongourl = "mongodb+srv://akakak:akakak@cluster0.b6pgq.mongodb.net/?retryWrites=true&w=majority"
lm = settings["discordbot"]["lastmsg"]
new_db_name = 'others'
default_collection_name = 'default'
collection_name = settings["discordbot"].get("database_Name", default_collection_name)

try:
    print(f'{Clr.CYN}{Clr.BLD}Establishing connection to database..{Clr.RST}')
    mgclient = MongoClient(mongourl)
    new_db = mgclient[new_db_name]
    Banlist = new_db[collection_name]
    #dbname = mgclient['vortex']
    #banlist = dbname['bans']
    #mutelist =dbname['muts']
    comp_list=new_db['comp']
    notify_list=new_db['notify']
    complaint_count=new_db['complainter']
    complaints_count=new_db['complaints']
    playerinfo=new_db['pinfo']
    collection=new_db['cards']
    print(f'{Clr.CYN}{Clr.BLD}Succesfully connected to database!{Clr.RST}')
    print(f'{Clr.CYN}{Clr.BLD}Database Name: {collection_name}{Clr.RST}') 
    print(f'{Clr.CYN}{Clr.BLD}Join us on discord : vortex and honor paradise{Clr.RST}')                                                                                                                
except Exception as err:
    print(f'{Clr.RED}{Clr.BLD}Connection to database failed:\n{err}{Clr.RST}')
    print(f'{Clr.RED}{Clr.BLD}Many features like ban will be non functioning!')

        