import logging.handlers

handler = logging.handlers.SMTPHandler(("smtp.qiye.aliyun.com","25"),"from_addr",["to_addr"],"SUBJECTS_PYTHON",
                                       ("username","password"))
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.addHandler(handler)

logger.warning("this is from python!!!!!!")
