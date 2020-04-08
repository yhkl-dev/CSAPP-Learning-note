;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname prac_fib) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (f n)
  (f-iter 2 1 0 n)
  )

(define (f-iter a  b c n)
  (if (= n 0)
      c
      (f-iter (+ a (* 2 b) (* 3 c)) a b (- n 1))))
