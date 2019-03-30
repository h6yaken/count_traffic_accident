#!/bin/bash
set -e

function main () {
  # 0 12 * * * /home/[User]/count_traffic_accident/script/run.sh >> /home/[User]/count_traffic_accident/accident.log
  # 上記のようにcronを設定した場合、ディレクトリの移動が必要
  cd /home/kento-hayakawa/count_traffic_accident

  python3 -m venv venv
  source venv/bin/activate

  # cronのログに不要な文字列を出力しないようにする
  # 初回のみ実行でよい
  # pip install -r requirements.txt
  
  python3 -m count_traffic_accident

  deactivate
}

main $?
