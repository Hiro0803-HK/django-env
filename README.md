# マニュアル

### 使用しているもの
    Visual Studio Code
    Windows Subsystem for Linux2 (WSL2)
    Remote Development 
    Python3-11(Dockerfileより使用)
    Docker Desktop(docker)
    docker-compose
    nginx(コンテナ)
    Django(コンテナ)
    PostgreSQL(コンテナ)
    uwsgi
    
### ソースコードの説明
    隠しディレクトリ.devcontainerにymlファイル、同階層のwebディレクトリにDockerfileを配置することで拡張機能Remote Developmentより、VSCode内でコンテナを起動しています。
    devcontainer.jsonファイルでコンテナ内のVSCodeで利用するディレクトリ、コンテナの名前、各種拡張機能を決定しています。
    requirements.txtはコンテナ環境作成時に利用するサービスを書いており、Dockerfileのコマンド実行と連動させています。

    dbディレクトリはローカルにマウントするディレクトリを配置しています。

    nginxディレクトリにはnginxの各種設定ファイルを配置しています。
    uwsgi_paramとssl_certsはHTTPS通信をする際に使用するコンテナhttps-portalに必要な設定とssl_keyのマウントディレクトリで、今の所は使用予定はありません。

    webディレクトリはコンテナ内での作業内容をマウントするファイルをです。(今回はDjangoの作業内容)
    隠しディレクトリ.vscodeはVSCodeでデバック実行するための設定ファイルが格納されています。

    staticディレクトリはnginxにadminページを反映させるために用意しました。この中にadminページのデータが格納されています。

    
### 今後の予定    
    第一クールはコンテナ通信を利用したVSCodeでの環境作成までなので、Djangoの開発は第二クールに行います。




#### 最終更新

    ログイン機能を実装し、ログイン後の画面を追加しました。
    今後使用する可能性のあるデータベースを作成しました。(models.py)