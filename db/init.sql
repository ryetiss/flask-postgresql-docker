CREATE TABLE public.users(
	id			integer	PRIMARY KEY	NOT NULL,
	username	varchar(100)	NOT NULL,
	password	varchar(100)	NOT NULL
);

CREATE TABLE public.newsletters(
	id		integer	PRIMARY KEY	NOT NULL,
	header	varchar(100)	NOT NULL,
	body	varchar(500)	NOT NULL,
	topic	varchar(100)	NOT NULL,
	author	varchar(100)	NOT NULL
);

INSERT INTO public.users VALUES(1,'admin','sha256$bCyCvz539UTc7yby$1745cb97d90bd1ed02af810022f0eb4b877f13efa369077982081a43b747fcb7');