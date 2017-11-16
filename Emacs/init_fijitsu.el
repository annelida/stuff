(put 'upcase-region 'disabled nil)
(desktop-save-mode 1)
(tool-bar-mode -1)
(menu-bar-mode -1)
(scroll-bar-mode -1)
(setq sentence-end-double-space nil)
;;
(require 'package)
(add-to-list 'package-archives '("org" . "http://orgmode.org/elpa/") t)
;; and MELPA
(add-to-list 'package-archives
             '("melpa" . "https://melpa.org/packages/") t)
(when (< emacs-major-version 24)
  ;; For important compatibility libraries like cl-lib
  (add-to-list 'package-archives '("gnu" . "http://elpa.gnu.org/packages/")))
;;
(global-set-key (kbd "C-x g") 'magit-status)
;;
(org-babel-do-load-languages
 'org-babel-load-languages
 '((python . t)
   (emacs-lisp . t)
   (sh . t)
   (js . t)
   (ditaa . t)
   (plantuml . t)
   (sqlite . t)
   ))
;;
(package-initialize)
;; 
(require 'org-bullets)
(add-hook 'org-mode-hook (lambda () (org-bullets-mode 1)))
;;
(require 'voca-builder)
(setq voca-builder/voca-file "/home/vikky/DVCS/stuff/vocabulary.org")
(setq voca-builder/export-file "~/.voca-builder-temp.org")
(setq voca-builder/current-tag "Study")
;; 
(require 'key-chord)
    (key-chord-mode 1)
    (key-chord-define-global "QQ"     'voca-builder/search-popup)
    (key-chord-define-global "FF"     'other-frame)
    (key-chord-define org-mode-map "DD"     'org-drill)
    (key-chord-define org-mode-map "AA"     'org-drill-again)
    (key-chord-define org-mode-map "RR"     'org-drill-resume)
;;
;;
;; (setq org-default-notes-file (concat org-directory "/notes.org"))
;; (define-key global-map "\C-cc" 'org-capture)

;; (setq org-capture-templates
;;       '(("p" "Todo" entry (file+headline "~/org/gtd.org" "Tasks")
;; 	 "* TODO %?\n  %i\n  %a")
;; 	("i" "Idiom" entry (file+datetree "/home/vikky/Desktop/DVCS/org/idioms.org")
;; 	 "* %i\n %U")
;; 	;;
;; 	("t" "Thought" entry (file+datetree "/home/vikky/Desktop/DVCS/org/thoughts.org")
;; 	 "* %?%c\n%i\n %l")
;; 	;;
;; 	("j" "Journal" entry (file+datetree "~/org/journal.org")
;; 	    "* %?\nEntered on %U\n  %i\n  %a")))
;; (custom-set-faces
;;  ;; custom-set-faces was added by Custom.
;;  ;; If you edit it by hand, you could mess it up, so be careful.
;;  ;; Your init file should contain only one such instance.
;;  ;; If there is more than one, they won't work right.
;;  )
;;
(setq elfeed-feeds
       '("http://nullprogram.com/feed/"
         "http://planet.emacsen.org/atom.xml"
	 "http://emacsrocks.com/atom.xml"
	 "http://0--key.github.io/rss.xml"
	 "http://www.quora.com/rss"))
(global-set-key (kbd "C-x w") 'elfeed)
;;
(setq org-agenda-files (list "/home/vikky/DVCS/stuff/edu.org"
 			     "/home/vikky/DVCS/stuff/vocabulary.org"
 			     "/home/vikky/DVCS/stuff/projects/2017/amazon/description.org"))
(define-key global-map "\C-ca" 'org-agenda)
(setq org-log-done t)
;;
(desktop-save-mode 1)
;;
(require 'google-translate)
(require 'google-translate-default-ui)
(global-set-key "\C-ct" 'google-translate-at-point)
(global-set-key "\C-cT" 'google-translate-query-translate)
(setq google-translate-default-source-language ' "en")
(setq google-translate-default-target-language ' "ru")
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(org-modules
   (quote
    (org-bbdb org-bibtex org-docview org-gnus org-info org-irc org-mhe org-rmail org-w3m org-drill)))
 '(package-selected-packages
   (quote
    (pyvenv voca-builder org-bullets magit key-chord howdoi google-translate go-autocomplete ereader elfeed color-theme))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
;;
(require 'org-drill)
(server-start)
