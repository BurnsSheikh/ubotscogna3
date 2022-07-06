from pyrogram import Client 

Client = Client(
    'nomesessione', #nome sessione
    session_string = 'AQBCJeroTFJa59H8q34FfILae5h_50o2eqlZEtDxcUJufdvm8B052J0Z3LtWVd1jUrrdnG-VaEI65GowdWg_gHejhaklQy9eD8OcFoAmcc51piKzstXvU42DxPWd4oUCVJM7TbRtzEShaXBQwmkcqyLu8-KrXAjLPISAuJB024ZRMFp66kcDtOt3oDaOwigjZV0_TmTwdnaKnIQrwkiS0OqzZjvTCIbarfg0GUnz-MpRY_GBws3mmD-bq1Z1NjjWUzfGxWT19PbojEMDWQ_HOClgbeiVdfHu1a3GXIJDLoASB0ByBRd5LeGON5zMOtqpPIrJzzOlTPmlx75XaapDAigRciqQNQA', #string session che ricavi da generatorestring.py avviandolo
    api_id = 123, #api id che prendi da my.telegram.org
    api_hash = "123abc", #api hash che prendi da my.telegram.org
    plugins = dict(root="plugins") #cartella dei plugins
)

if __name__ == "__main__":
    Client.run()
