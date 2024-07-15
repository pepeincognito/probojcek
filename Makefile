
CLEAN = hrac klient.tar.gz

DIR != basename `pwd`

Color_Off='\033[0m'
Black='\033[1;30m'
Red='\033[1;31m'
Green='\033[1;32m'
Yellow='\033[1;33m'
Blue='\033[1;34m'
Purple='\033[1;35m'
Cyan='\033[1;36m'
White='\033[1;37m'

SOURCES=$(wildcard *.py)

all: hrac klient.tar.gz
naserveri: hrac

klient.tar.gz: hrac
	@echo -e $(Yellow)"Creating "$(Green)$(DIR)$(Yellow)" tar for upload"$(Color_Off)
	@tar czf $@ $(addprefix --exclude=,$(CLEAN)) *
	@echo -e $(Green)$(DIR)$(Yellow)" tar created successfully!"$(Color_Off)

hrac: $(SOURCES)
	@echo -e $(Blue)"Python creating "$(Green)$(DIR)$(Color_Off)
	@install -m 755 hrac.py hrac
	@echo -e $(Blue)"Python created "$(Green)$(DIR)$(Blue)" successfully!"$(Color_Off)

clean:
	@-rm -f $(CLEAN)
	@echo -e $(Purple)$(DIR)$(Cyan)" cleaning Complete!"$(Color_Off)
