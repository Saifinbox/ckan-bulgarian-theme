# Визуална тема на портала за отворени данни

В това хранилище е кодът на визуалната тема, използвана на [българския портал за отворени данни](https://opendata.government.bg).

За другите компоненти, съставящи портала, вижте [събирателното хранилище governmentbg/opendata](https://github.com/governmentbg/opendata).

## Стилове (CSS)

Стиловете в тази тема са написани на [SCSS](http://sass-lang.com/) и използват [Compass](http://compass-style.org/). Намират се в [ckanext/bulgarian_theme/fanstatic/extra.scss](ckanext/bulgarian_theme/fanstatic/extra.scss). За да ги променяте, е необходимо първо да имате инсталиран Compass. [Инструкции за това има тук](http://compass-style.org/install/).

Промените трябва да се правят по `.scss`-версията на файла, а не по резултатния `.css` файл.

Може да използвате следната команда, изпълнена от папката на проекта, за да генерирате автоматично `.css` файлове от променените `'.scss' оригинали:

    compass compile --output-style expanded --sourcemap --no-line-comments --sass-dir ckanext/bulgarian_theme/fanstatic --css-dir ckanext/bulgarian_theme/fanstatic
