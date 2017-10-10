# -*- coding: utf-8 -*-

WEEK_SALE_INFO = 'week:sale:info:%s:%s'  # HASH， Week.thisweek().isoformat(), product_id， {uid-sale}
WEEK_CHAMPION_INFO = 'week:champion:info:%s:%s'  # STRING， Week.thisweek().isoformat(), product_id， '{'avatar': '', 'desc': ''}'

TOTAL_LEFT_BALANCE = 'total:left:balance'  # STRING，

BALANCE_WITHDRAW_REQUEST_QUEUE = 'queue:pocket:request'  # 余额提现请求队列
BALANCE_WITHDRAW_RESULT_QUEUE = 'queue:rebate:balance:withdraw:result'  # 余额提现结果队列
BALANCE_WITHDRAW_RESULT_HASH = 'hash:rebate:balance:withdraw:result'  # HASH, 余额提现结果
