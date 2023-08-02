```sh
$ snscrape --jsonl twitter-user utaubot > @utaubot.json
$ snscrape --jsonl twitter-search 'from:tb2g_vocaloid nicovideo' > '@tb2g_vocaloid nicovideo.json'
$ for file in @*.json; do; jq -s "[.[] | .rawContent, .outlinksss]" $file > slim-$file; done
$
$ # @utaunow.json was downloaded earlier
$ for file in @utaunow.json; do; jq -s "[.[] | .content, .outlinks[0]]" $file > slim-$file; done
$
$ # jq won't read the whole file??
$ for file in /tmp/@vocaloid_fm.json; do; tail -n+000000 $file | head -n100000 | jq -s "[.[] | .rawContent, .outlinksss]" > tail+000000-head100000-slim-@vocaloid_fm.json; done
$ for file in /tmp/@vocaloid_fm.json; do; tail -n+100000 $file | head -n100000 | jq -s "[.[] | .rawContent, .outlinksss]" > tail+100000-head100000-slim-@vocaloid_fm.json; done
$ for file in /tmp/@vocaloid_fm.json; do; tail -n+200000 $file | head -n100000 | jq -s "[.[] | .rawContent, .outlinksss]" > tail+200000-head100000-slim-@vocaloid_fm.json; done
$ for file in /tmp/@vocaloid_fm.json; do; tail -n+300000 $file | head -n100000 | jq -s "[.[] | .rawContent, .outlinksss]" > tail+300000-head100000-slim-@vocaloid_fm.json; done
$ for file in /tmp/@vocaloid_fm.json; do; tail -n+400000 $file | head -n100000 | jq -s "[.[] | .rawContent, .outlinksss]" > tail+400000-head100000-slim-@vocaloid_fm.json; done
$ for file in /tmp/@vocaloid_fm.json; do; tail -n+500000 $file | head -n100000 | jq -s "[.[] | .rawContent, .outlinksss]" > tail+500000-head100000-slim-@vocaloid_fm.json; done
$ for file in /tmp/@vocaloid_fm.json; do; tail -n+600000 $file | head -n100000 | jq -s "[.[] | .rawContent, .outlinksss]" > tail+600000-head100000-slim-@vocaloid_fm.json; done
```

```
snscrape --jsonl twitter-user vocaloid_fm > vocaloid_fm.json  887.91s user 22.16s system 6% cpu 3:39:15.37 total
```
3 entire hours yippee

raw data: https://github.com/szc126/metadata-nnd-vocalo-twitter/releases/tag/v1