# Recipe Web App

## Overview  

This project is a simple web application designed to store, display, and manage recipes. It is built using **Django and SQLite**, and hosted on a **Raspberry Pi**, making it easily accessible from any device on your **local network**, including phones, tablets, and laptops.  

## Stack  

- **Frontend**: Django Templates + Bootstrap  
- **Backend**: Django  
- **Database**: SQLite  
- **Server**: Django Development Server (for local testing), Gunicorn + Nginx (for production)  
- **Hosting**: Raspberry Pi  

## Features  

- Add, view, and manage recipes with ease.  
- Accessible from any device on the local network.  
- Secure access with Django’s built-in authentication system.  
- Lightweight and efficient, suitable for Raspberry Pi deployment.  

## Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.

## Setting up Requirements
(putting this here partially for myself because i keep forgetting these commands)

to install the dependencies from the requirements.txt file:
```bash
pip install -r requirements.txt
```

to freeze/ update dependencies into the text file run :
```bash
pip freeze > requirements.txt
```
