import collections
import os

import arrow

last_week = arrow.now().shift(days=-7)
mod_last_week = collections.defaultdict(int)

for route in os.listdir():
    mod_epoch = os.path.getmtime(route)
    mod_time = arrow.get(mod_epoch, tzinfo="Atlantic/Canary")
    if mod_time > last_week:
        mod_last_week[mod_time.date()] += 1

for key in sorted(mod_last_week):
    print(f"{key} {mod_last_week[key] * '▉'}")
