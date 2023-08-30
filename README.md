
# Aircraft Maintenance Taskaid

This is a CLI (Command line interface) based app written in Python. This app is used to support Aircraft Technicians (Any Technicians) to keep track Maintenance tasks to aid them with their day to day work in a fast paced environment without constantly looking at paper work packages.  


## Acknowledgements

 - [Flatiron School](https://flatironschool.com/) - For Bootcamp and Education
 - [SQLAlchemy](https://docs.sqlalchemy.org/en/14/) - SQLAlchemy documentation 
 - [Google](https://www.google.com) - Searching aid for things unknown
 - [github](https://github.com) - For Repositories and enable collaboration
 - [readme.so](https://readme.so) - README template
 - [Text to ASCII Art Generator (TAAG)](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) - Text to ASCII Generator to create text based banners
 - [prettycli](https://github.com/noyoshi/prettycli) - Make print() statements colorful
 - [Simple Terminal Menu](https://github.com/IngoMeyer441/simple-term-menu) - Create interactive menu items for Command Line interface

## API Reference

Both JSON files were used to seed aircraft.db database file.
No external APIs were used. They were locally created with sample aircraft models and maintenance tasks.

#### Get all items

```http://localhost:3000/aircraft
  GET /${id}
  GET /${make}
  GET /${model}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Get item

```http://localhost:3001/aircraft_tasks
  GET /${id}
  GET /${ata_chapter_number}
  GET /${ata_chapter_name}
  GET /${tasks}

```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Get item




## Authors

- [Jiyong Kim](https://github.com/jiyongk84)




## Installation and running the app
Fork my repo:
- [github](https://github.com/jiyongk84/flatiron-phase3-project-jyk)

```bash
  git clone (forked link)

  cd flatiron-phase3-project-jyk/lib

  pipenv shell

  python3 -m pip install prettycli

  python3 -m pip install simple-term-menu

  python3 cli.py
```
    
## Screenshots

![App Screenshot](https://github.com/jiyongk84/flatiron-phase3-project-jyk/blob/main/lib/flatiron-phase3-project%20sample.png)


## License

[MIT](https://choosealicense.com/licenses/mit/)

