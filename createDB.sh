#!/bin/sh
MYUSER=root
MYPASS=Qaz520..
DBNAME=xxq
mysql -u $MYUSER -p$MYPASS
CREATE DATABSAE $DBNAME
USE $DBNAME
CREATE TABLE IF NOT EXISTS serve(
    client_id INT UNSIGNED NOT NULL,
    arrive_time INT UNSIGNED,
    interval_time INT UNSIGNED,
    serve_time INT UNSIGNED,
    serve_start_time INT UNSIGNED,
    wait_time INT UNSIGNED,
    serve_end_time INT UNSIGNED,
    spend_time INT UNSIGNED,
    sys_free_time INT UNSIGNED,
    avg_wait_time INT_UNSIGNED,
    sys_util INT UNSIGNED,
    PRIMARY KEY (client_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8
