from bottle import route, run, template


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


run(host='localhost', port=8080)


def main():
    '''
    主函数
    '''
    pass


if __name__ == "__main__":
    main()
