let s:path = fnamemodify(resolve(expand('<sfile>:p')), ':h') . '/aliapath.py'

function! OpenPath ()
  execute 'py3file ' . s:path
endfunction

command! OpenPath call OpenPath()
