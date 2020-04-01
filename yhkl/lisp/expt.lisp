;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname expt) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (expt-1 b n)
  (if (= n 0)
      1
      (* b (expt b (- n 1)))))

(define (expt-2 b n)
  (expt-iter-2 b n 1))
(define (expt-iter-2 b counter product)
  (if (= counter 0)
      product
      (expt-iter-2 b (- counter 1) (* b product))))

(define (fast-expt b n)
  (cond ((= n 0) 1)
        ((even-new? n) (square (fast-expt b (/ n 2))))
        (else (* b (fast-expt b (- n 1))))))

(define (square x) (* x x))

(define (even-new? n)
  (= (remainder n 2) 0))