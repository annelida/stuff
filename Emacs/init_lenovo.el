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
(setq voca-builder/voca-file "/home/vikky/Desktop/DVCS/stuff/vocabulary.org")
(setq voca-builder/export-file "~/.voca-builder-temp.org")
(setq voca-builder/current-tag "Study")
;; 
(require 'key-chord)
    (key-chord-mode 1)
    (key-chord-define-global "QQ"     'voca-builder/search-popup)
    (key-chord-define-global "FF"     'other-frame)
;;
;; (require 'ereader)
;; ;; end of custom vars
;; ;; use org-bullets-mode for utf8 symbols as org bullets
;; (require 'org-bullets)
;; (add-hook 'org-mode-hook (lambda () (org-bullets-mode 1)))
;; ;;
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
;; (package-initialize)
;; (elpy-enable)
;; ;;
;; (require 'key-chord)
;;     (key-chord-mode 1)
;;     (key-chord-define-global "QQ"     'voca-builder/search-popup)
;;     (key-chord-define-global "FF"     'other-frame)
;; ;;
;; (setq elfeed-feeds
;;       '("http://nullprogram.com/feed/"
;;         "http://planet.emacsen.org/atom.xml"
;; 	"http://emacsrocks.com/atom.xml"
;; 	"http://0--key.github.io/rss.xml"
;; 	"http://www.quora.com/rss"
;; 	"https://www.upwork.com/ab/feed/jobs/rss?proposals=0-4&q=Amazon+API&sort=relevance+desc&api_params=1&securityToken=1461ab4f14c4bbd50764489ba49f4d11ed155685db667cac84e7c2655ee3c6999ac378f96c0b7205e6a0fd7521cd20dc9463c63389b9fc837e65b6bdee91c5c9&userUid=562235792203943936&orgUid=562235792216526849"
;; 	"https://www.upwork.com/ab/feed/jobs/rss?proposals=0-4&q=Python&sort=relevance+desc&api_params=1&securityToken=1461ab4f14c4bbd50764489ba49f4d11ed155685db667cac84e7c2655ee3c6999ac378f96c0b7205e6a0fd7521cd20dc9463c63389b9fc837e65b6bdee91c5c9&userUid=562235792203943936&orgUid=562235792216526849"
;; 	"https://www.upwork.com/ab/feed/jobs/rss?proposals=0-4&q=Python+Scrapy&sort=relevance+desc&api_params=1&securityToken=1461ab4f14c4bbd50764489ba49f4d11ed155685db667cac84e7c2655ee3c6999ac378f96c0b7205e6a0fd7521cd20dc9463c63389b9fc837e65b6bdee91c5c9&userUid=562235792203943936&orgUid=562235792216526849"))
;; (global-set-key (kbd "C-x w") 'elfeed)
;;
(setq org-agenda-files (list "/home/vikky/Desktop/DVCS/stuff/edu.org"
 			     "/home/vikky/Desktop/DVCS/stuff/vocabulary.org"
 			     "/home/vikky/Desktop/DVCS/stuff/projects/2017/amazon/description.org"))
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
