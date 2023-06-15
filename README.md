# マニュアル

### 使用しているもの
    Visual Studio Code
    WSL2
    Remote Development 
    Python3-11
    Docker Desktop(docker)
    docker-compose
    nginx(コンテナ)
    Django(コンテナ)
    PostgreSQL(コンテナ)
    uwsgi
    
### ソースコードの説明
    隠しディレクトリ.devcontainerにymlファイル、同階層のwebディレクトリにDockerfileを配置することで拡張機能Remote Developmentより、VSCode内でコンテナを起動している。
    devcontainer.jsonファイルでコンテナ内のVSCodeで利用するディレクトリ、コンテナの名前、各種拡張機能を決定する。
    requirements.txtはコンテナ環境作成時に利用するサービスを書いており、Dockerfileのコマンド実行と連動させている。

    dbディレクトリはローカルにマウントするディレクトリを配置している。

    

