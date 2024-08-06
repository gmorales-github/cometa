#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config.LoggerConfig import LoggerConfig
from config.constants import TITLE_SCREEN
from appgame.PygameApp import PygameApp


def main():
    """ Main program """

    # Logger default lvl = DEBUG
    logger_config = LoggerConfig('logger')
    logger = logger_config.get_logger()


    logger.info("--- Start ---")

    # app pygame object
    app = PygameApp(640, 480, TITLE_SCREEN)
    app.run()

    logger.info("--- End ---")

if __name__ == '__main__':
    main()