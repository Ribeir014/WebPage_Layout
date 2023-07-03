from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)   #o debug:sempre que fazemos uma mudança no código vai dar rerun o servidor web