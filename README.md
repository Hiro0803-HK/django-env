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
    トップページに表示するコンテンツを作成していきます。




#### 最新の更新
    ログインフォームを作成し、ログイン、ログアウト、サインアップの機能を追加しました。
    ログイン専用のアプリケーションaccountsを作成しました。(djangoのテンプレートも一部使用しています。)
    サインアップを行うと、データベースにユーザーネームが格納されます。
