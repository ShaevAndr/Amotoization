# Скрипт автоматической заливки обновлений виджета на сервер. Автоматически обновляет manifest.json и заливает новое обновление.

### При запуске скрипта открывается окно Chrom а доходит до страницы данных выджета. Далее программа ждёт нажатия Enter в командной строке. ПРоисходит обновление виджета в системе. 
### Далее скрипт продолжает работать и ждёт следующей команды (нажатия Enter) для обновления.

## Настройки программы:
> Файл serverUpdate.py:
>> EMAIL = 'почта@gmail.com'

>> PASSWORD = "пароль"

>> PATH_TO_WIDGET_ZIP = путь к файлу widget.zip. Например "C:\\widget\\widget.zip"

>> WIDGET_CLASS =  класс виджета на странице установленных интеграций. Например:"agitq3-7Fh6"

> Файл update.py:
>> PATH = путь к каталогу с виджетом. Например "C:\\widget\\" (в папке widget лежат уже именно файлы виджета).

## Установка:

> Установка Python версии 3.10+
>> Ссылка https://www.python.org/

>> При установке дать согласие на запись Python в PATH

> Установка Selenium 
>> В командной строке прописать pip install selenium

> Установка драйвера Chrome 

>> Из списка выбрать драйвер такой же версии, как и хром на компьютере https://chromedriver.storage.googleapis.com/index.html

>> Распаковать в директорию со скриптами.

## Запуск:

> Запуск командой python serverUpdate.py


