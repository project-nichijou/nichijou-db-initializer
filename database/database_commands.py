
CREATE_TABLE_COMMANDS = {
	'CREATE_TABLE_ANIME': (
		'CREATE TABLE IF NOT EXISTS `anime` ('
		'	`nid`			INT UNSIGNED NOT NULL,'
		'	PRIMARY KEY ( `nid` )'
		') ENGINE=InnoDB CHARSET=utf8mb4'
	),
	'CREATE_TABLE_ANIME_NAME': (
		'CREATE TABLE IF NOT EXISTS `anime_name` ('
		'	`nid`			INT UNSIGNED NOT NULL,'
		'	`name`			VARCHAR(200) NOT NULL,'
		'	PRIMARY KEY ( `nid`, `name` )'
		') ENGINE=InnoDB CHARSET=utf8mb4'
	),
	'CREATE_TABLE_EPISODE_NAME': (
		'CREATE TABLE IF NOT EXISTS `episode_name` ('
		'	`nid`			INT UNSIGNED NOT NULL,'
		'	`type`			INT UNSIGNED NOT NULL,'
		'	`sort`			INT UNSIGNED NOT NULL,'
		'	`name`			VARCHAR(200) NOT NULL,'
		'	PRIMARY KEY ( `nid`, `type`, `sort`, `name` )'
		') ENGINE=InnoDB CHARSET=utf8mb4'
	),
	'CREATE_TABLE_MATCH_FAIL': (
		'CREATE TABLE IF NOT EXISTS `match_fail` ('
		'	`id`			INT UNSIGNED NOT NULL,'
		'	`source`		VARCHAR(40) NOT NULL,'
		'	`dis`			LONGTEXT NOT NULL,'
		'	PRIMARY KEY ( `id`, `source` )'
		') ENGINE=InnoDB CHARSET=utf8mb4'
	),
	'CREATE_TABLE_CONFLICT': (
		'CREATE TABLE IF NOT EXISTS `conflict` ('
		'	`nid`			INT UNSIGNED NOT NULL,'
		'	`field`			VARCHAR(40) NOT NULL,'
		'	PRIMARY KEY ( `nid`, `field` )'
		') ENGINE=InnoDB CHARSET=utf8mb4'
	),
	'CREATE_TABLE_REVISE': (
		'CREATE TABLE IF NOT EXISTS `revise` ('
		'	`nid`			INT UNSIGNED NOT NULL,'
		'	`field`			VARCHAR(40) NOT NULL,'
		'	`target`		VARCHAR(40),'
		'	`value`			LONGTEXT,'
		'	PRIMARY KEY ( `nid`, `field`, `target` )'
		') ENGINE=InnoDB CHARSET=utf8mb4'
	),
	'CREATE_TABLE_SITES': (
		'CREATE TABLE IF NOT EXISTS `sites` ('
		'	`name`			VARCHAR(40) NOT NULL,'
		'	`urlTemplate`	LONGTEXT NOT NULL,'
		'	`regions`		LONGTEXT NOT NULL,'
		'	PRIMARY KEY ( `name` )'
		') ENGINE=InnoDB CHARSET=utf8mb4'
	),
	'CREATE_TABLE_SOURCES': (
		'CREATE TABLE IF NOT EXISTS `sources` ('
		'	`name`			VARCHAR(40) NOT NULL,'
		'	`url`			LONGTEXT NOT NULL,'
		'	PRIMARY KEY ( `name` )'
		') ENGINE=InnoDB CHARSET=utf8mb4'
	),
	'CREATE_TABLE_LOG': (
		'CREATE TABLE IF NOT EXISTS `log` ('
		'	`time`		DATETIME NOT NULL,'
		'	`content`	LONGTEXT NOT NULL'
		') ENGINE=InnoDB CHARSET=utf8mb4'
	)
}
