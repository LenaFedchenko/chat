import project

def main():
    try: 
        project.execute()
        project.socketio.run(project.project, debug=True, port=8000, allow_unsafe_werkzeug=True)
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()
