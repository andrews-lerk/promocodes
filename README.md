# Generate promocodes 
### Installing
- Update pip and install virtual enviroment
```
$ sudo -H pip3 install --upgrade pip
$ sudo -H pip3 install virtualenv
```
- Create virtual enviroment and activate
```
$ virtualenv .env
$ source .env/bin/activate
```
- Make ```git clone```
```
(.env) $ git clone https://github.com/andrews-lerk/promocodes.git
```
- cd project directory and make ```pip install```
```
(.env) $ cd promocodes
(.env) $ pip install -r requirements.txt
```
### Usage
- To generate promocodes use:
```
(.env) $ python manage.py generate_code --amount {amount of codes} --group {name of group}
```
or
```
(.env) $ python manage.py generate_code -a {amount of codes} -g {name of group}
```
that's create a directory 'promocodes_storage' with json file
- To check promocode use:
```
(.env) $ python manage.py check_code {your code}
```
that's return 'Код существует группа = {group}' or 'Код не существует'
- Use django test:
```
(.env) $ python manage.py test main.tests.GeneratePromocodesCase.generate
```
that's call commands:
```python
generate_promocodes(amount=10, group='агенства')
generate_promocodes(amount=1, group='агенства')
generate_promocodes(amount=42, group='avtostop')
generate_promocodes(amount=5, group=1)
```
