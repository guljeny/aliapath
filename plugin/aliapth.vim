let s:defaultConfig = {'^\(.*\)$': '\1.js'}
let g:aliapath_entries ={}

let g:aliapath_entries = {'^utils\(.*\)$': './apps/utils\1.js'}

function OpenPath ()
  let filename = expand('%:e') 
  if filename != 'js'
    return
  endif

  normal! vi"
  normal! "zy

  let filepath = @z
  let config = extend(g:aliapath_entries, s:defaultConfig)

  for conf in items(config)
    if matchstr(filepath, conf[0]) != ""
      let path = substitute(filepath, conf[0], conf[1], "g")
      if filereadable(path)
      " normal! e path
        echo path
        execute "e " . fnameescape(path)
        return
      endif
    endif
  endfor
endfunction

command! OpenPath call OpenPath()
