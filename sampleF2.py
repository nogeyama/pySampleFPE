# -*- coding: utf-8 -*-
# どこかの行/最初の行には日本語を埋めておこう.SJISでないことを判別できるように．
# 
# 目的：
#
# 機能
#
# フォルダ文字として以下は禁止
# \/:*?"<>|
# 
# フォルダ文字として以下は可能で，要注意
# SP'$\
# 
# 文字列中の' ', '$', '`', '\' にはESC文字('\')を付与する．
# 文字列全体は""で囲む．
# 
# とりあえず，以下のフォルダ名を挟んだファイルがアクセスできるか？
# sp'$
# 
# 日本語SP SQ' EV$PATH +
# 
# azAZ09@_$#%&! =-+.,;'`(日){本}[語]~^
# 


import codecs
if __name__ == '__main__':

    fp_in_sjis2unicode = codecs.open(u'data-in-sjis.txt','r','shift_jis')
    fp_out_unicode2utf8 = codecs.open(u'data-out-utf8.txt','w','utf-8')

    for row in fp_in_sjis2unicode:
        print type(row),'row=unicode'

        rowJunicode = u'追加プログラム内文字列1--'+row  # MIX!★
        print type(rowJunicode),'rowJunicode=unicode'

        ##rowJstr = rowJunicode.encode('utf-8') # 直前に一括して変換．（途中で変換して結合はダメ）
        rowJstr = rowJunicode.encode('shift_jis') # 直前に一括して変換．（途中で変換して結合はダメ）
        print rowJstr  # ==> できた！consoleOK&pipeOK&writeNG as str
        print type(rowJstr),'rowJstr=str'

        fp_out_unicode2utf8.write(rowJunicode)  # writeOK as Unicode

    fp_out_unicode2utf8.write(u'追加プログラム内文字列2')  # < writeOK as Unicode！
    print u'追加プログラム内文字列3'.encode('shift_jis')

    fp_in_sjis2unicode.close()
    fp_out_unicode2utf8.close()

#
#
# まとめ
# ・内部表現（unicode）と外部表現（str）は混ぜない．
#   外部表現はすぐ内部表現に変換し，
#   外部に出力する際は，直前で外部表現に一括変換する．
#   変数のデフォルト型は内部表現unicodeに統一する．
#   （これと反対にstrを基準にすることも不可能ではないし，一見楽．
#     しかし，視点が逆になるのでその人々（の記事）とコミュニケーションをするのは難しい．）
# ・print用の.encode('utf-8')は直前に一括して変換すべし．
# ・python2.7はdefaultcodingがasciiであるため自動変換でERRORが発生する．
#   自動変換が発生しないようにコーディングする必要がある．
# ・print,pipeはstrで出力．
#   printやpipeは明示的にencodeしないとダメ．
# ・writeはunicodeで出力 （これ紛らわしい）．
#   出力はunicodeを与えればよい．
#   codecs.open（fp）を経由するものは入力unicodeが指定文字コードに自動変換される．
# ・printがpipeに比べて少し柔軟，かつ，ロケールへの変換であって，defaultcodingではないので，より混乱する．
#   リダイレクトした途端にERRORが発生してしまう．
#   pipeの動作も常に確認すべき．
# ・python3では，defaultcodingがutf-8になるので，
#   環境，プログラム，データの全てがutf-8環境の場合楽ちんになる．
#   しかし，python2.7との互換性問題が出る．
#
# 作法
#・外部表現strの文字列にはstrをつける．
#

