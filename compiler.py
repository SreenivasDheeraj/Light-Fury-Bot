import requests

url = 'https://api.jdoodle.com/v1/execute'

s = """
(defun format-date (s) (format t "~A~A~A~%" (subseq s 6 10) (subseq s 3 5) (subseq s 0 2)))

(format-date "11/12/2019")
(format-date "12/31/2019")
(format-date "01/15/2019")
(terpri)

(defun is-palindrome-possible (s)
  (setq a (sort (copy-seq s) #'char>))
  (setq cnt 0)
  (loop for x from 0 to (- (length s) 2)
        do (if (string= (elt a x) (elt a (+ 1 x)))
             (incf cnt)))
  (if (= (length s) (+ (* cnt 2) 1))
    (write-line "true")
    (write-line "false")))

(is-palindrome-possible "rearcac")
(is-palindrome-possible "suhbeusheff")
(is-palindrome-possible "palindrome")
(terpri)
(defun farey (n)
    (if(/= n 1)
        (let ((a 0) (b 1) (c 1) (d n) k f e)
        (format t "~a/~a " a b)
        (loop while (< c n) do
            (setq 
            k (floor (/ (+ n b) d))
            e (- (* k c) a)
            f (- (* k d) b)
            a c
            b d
            c e
            d f)
        (format t "~a/~a " a b)))
    (format t "0/1 1/1~%")))

(farey 1)
(farey 4)
"""

params = dict(
    script = s,
    language= "clisp",
    versionIndex= "3",
    clientId= "15f5c12845b4488732977386a7dc47ec",
    clientSecret="258bdba6770d5bfb68904d6333c5130c6feb81b4447a63636687900185c41c37"
)

resp = requests.post(url=url, json=params)
data = resp.json() # Check the JSON Response Content documentation below
print(data['output'])