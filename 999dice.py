6�X^c           @   s!   d  d l  Z  e  j d � d Ud S(   i����NsK$  c        	   @   s�  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l m Z m	 Z	 m
 Z
 d  d l m Z d  d l m Z e j
 d e � e j d d � Z e j d d	 d
 d d d
 �e j �  Z e d d � � Z e j �  Z Wd QXe j e � Z e
 j e j d e
 j e j d e
 j e j d e
 j e j d e
 j  d e
 j e j d e
 j e j d e
 j e j! d e
 j e j d e
 j e j d e
 j e j d GHe
 j e j Z" e
 j  Z# e
 j e j Z$ e
 j e j Z% e
 j e j Z& e
 j e j! Z' e
 j e j! Z( e  j) �  Z* d Z+ i d d 6e d d 6d  d! 6d" d# 6d$ d% 6d& d' 6Z, d( �  Z- d) �  Z. d* �  Z/ e* j0 e+ d+ e, d, i d- d. 6d/ d0 6e d1 d2 d2 6e d1 d3 d3 6d4 d5 6�Z1 e j e1 j2 � Z3 y5 e" d6 e$ d e# e4 e5 e3 d7 d8 � d@ � GHWn d; GHe j6 �  n Xe5 e3 d7 d8 � dA e5 d< � k r�e" d= GHe j6 �  n  e/ e7 e5 e d> � dB � e7 e5 e d? � dC � � d S(D   i����N(   t   Foret   Backt   Style(   t   randint(   t   datetimet	   autoresett   descriptions<   999 Dice Bot | This Is Gambling Bot Plase Take Own Your Risks   -cs   --betsett   defaulti    t   helps%   Enter Your Betset Number (default: 0)s   config.jsont   rs�         ___  _           ___       __
     / _ \(_)______   / _ )___  / /_
    / // / / __/ -_) / _  / _ \/ __/
   /____/_/\__/\__/ /____/\___/\__/s)   
=======================================
s   Author By  s   : s   Kadal15
s   999 Dice Bots    | s   Lose Streak t   |s    Win Streak
s;   support by botakberambut(hijrah) And All Termux Id Member

s$   https://www.999doge.com/api/web.aspxs   file://t   Origins
   User-Agents
   user-agents!   application/x-www-form-urlencodeds   Content-types   */*t   Accepts#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   Accept-Languages   com.reland.relandicebots   X-Requested-Withc         C   s�   t  d t |  � d � } | d k s> | d k s> | d k r� t  | j d � d � } d t | � } t t | � d	 | � a d a n  | d
 k s� | d k s� | d k s� | d
 k s� | d k r� d a t | j d � d � a n  d  S(   Ni?B id   t   Hit   hit   HIt   .i   i   i
   t   Lot   LOWt   lowt   Lowt   LOi    (   t   strt   floatt   splitt   lent   intR   t   high(   t   persent   taruhant   ct   nt   pangkat(    (    t    t   konvert2   s    $	<c         C   s�   t  |  � d k  rI t d t  |  � � } | d t |  � }  d |  } n  t  |  � d k r� t d t  |  � � } | d t |  � }  d |  } n2 t  |  � } |  d } |  | d  } | d | } | S(   Ni   t   0s   0.i����R   (   R   R   R   (   t   numt   panjang_nolt   resultt   len_numt   endt   first(    (    R!   t   rev@   s    


c         C   s�
  t  j d k s- t  j d k s- t  j d k rt d } d } xG t rp | d 7} y t d | d } Wq< Pq< Xq< Wn t t  j � } t t d | d � d	 } t t d | d
 � d } t t t d | d � dP � } t t d | d t d | d d � | } i d d 6t d d 6| d 6t d 6t	 d 6t
 d d � d 6d d 6d d 6}	 yt j t
 d t d |	 �}
 t j |
 j � } | d t | d  � t | � } t | d  � t | � }
 t | d t | d  � t | � | � dQ } t d! t t t t | d � t |
 � � dR � GHd" t d | d GHd } t } t } t } t j �  j d# � } t | � t t d � } d } d } d } d } d } d$ } x�
t rj
t d | d% d& k s�t d | d% d' k s�t d | d% d( k rt j j d) � n1 | t t t d | d% � dS � k r=| } n  t d | d d* d+ d, k s�t d | d d* d+ d- k s�t d | d d* d+ d. k r�| d 7} | t k r&| t t d | d d* d/ � d k r�d0 } n  | t t d | d d* d/ � d1 d k r&d$ } d } q&n  | t k r�| t t d | d d* d2 � d k red0 } n  | t t d | d d* d2 � d1 d k r�d$ } d } q�q�n t d | d d } t  j d k s�t  j d k s�t  j d k r�t j �  j d# � } t | � t | d � k r�t | � t t d � } | d 7} | | k rUd } n  d3 t d | d d4 GHt t d | d � d	 } t t d | d
 � d } t t t d | d � dT � } q�n t t  j � } t d | d5 d+ d- k s1t d | d5 d+ d, k s1t d | d5 d+ d. k r't t j t t d | d5 d6 � t t d | d5 d7 � � d1 � } t t | � � } | d8 k r�t j j d9 t | � d: � n  | d; k r�t j j d9 t | � d< � n  | d= k rt j j d9 t | � d> � n  t | t | � � n t t d | d t | � � t  j! t | � � t | � } | d 7} i d d 6t d d 6| d 6t d 6t	 d 6t
 d d � d 6d d 6d d 6}	 | t t d? � k r�t d@ t dA t t | � GHt j" �  n  t j t
 d t d |	 �}
 t j |
 j � } t | d t | d  � t | � | � dU } t | d  � t | � }
 | d |  k r	t# dB t t | � t# dC t$ t t | � dV � t t t t | d � t |
 � � dW � t$ dD t t | � GHt dE GHt  j! d � t j" �  n  | d | k  r�	t# dB t t | � t# dF t% dG t t | � dX � t t t t | d � t |
 � � dY � t% dH t t | � GHt& j' t( j) dI GHt  j! d � t j" �  n  | d  d k	 r| d 7} d } t | d � t |
 � } | d k r�
t# dB t t | � t# dC t$ t t* t | � � � t+ dJ t t* t | � � � t+ dK t$ dL t t | � GHqNt# dB t t | � t# dC t$ t t* t | � � � t+ dJ t t* t | � � � t+ dK t% dH t t | � GHn?d } | d 7} d } t } t | d � t |
 � } | d k r�t# dB t t | � t# dF t% dG t t* t | � � � t+ dJ t t t* t | � � � t+ dK t$ dL t t | � GHn} t# dB t t | � t# dF t% dG t t* t | � � � t+ dJ t t t* t | � � � t+ dK t% dH t t | � GH| t k r�| d 7} t | � t t d | d2 � } | | k r�d } t } q�n= | | k r�d } | } n" t | � t t d | d/ � } | | k r
t } t } | d 7} n  | | k r+
t } t } | d 7} n  t j j t dM t t | � t, dN t t | � d9 � q�WWn dO GHt j" �  n Xd  S(Z   Nt   Autot   autot   AUTOi    i   t   Configs   Name Bet Sett   Intervali�  s   Reset If Wins   Base Beti
   i   t   Chancet   Bett   PlaceBett   at
   SessionCookiet   st   PayInR   t   Highi?B t
   ClientSeedt   doget   Currencyt   2t   ProtocolVersiont   headerst   datat   StartingBalancet   PayOuts   Starting Balance s   Anda Menggunakan BetSet Ke s   %MR
   s   Max Bett   OFFt   offt   OffR!   s   Hi / Lowt   Togglet   Ont   ONt   ons   If WinR   i   s   If Loses   Change Bet Set s                              s
   Random Chancet   Mint   Maxi   s   
s      i   s     i   t    s
   Target Profits%   
Yay.! 
Profit Mencapai Target.....!
s   Profit t   [s   ] t   Profits)   Yay.!
Balance Sudah Memenuhi Target.....!t   ]t   -s    Lose s   Lose Target....!s    [ s    ]s    Profit s   Win Streak s
    Lose Streak s   Beting stopi ��i ��i ��i ��i ��i ��i ��i ��i ��i ��(-   t   my_namespacet   betsett   Truet   objR   R   R"   t   jsR   R   R   R   t   postt   urlt   uat   jsont   loadst   textt   hijaut   resR   t   FalseR   t   nowt   strftimet   syst   stdoutt   writet   roundt   randomt   uniformR   t   timet   sleept   exitt   ungut   hijau2t   red2R   t   BRIGHTR    t   REDR*   t   abu2t   red(   t   wst   lst   urutt   jumlahulangt   pesant   slpt   limit_at   payint   amountR>   t   r1t   jsnt   jumblt   jumt   profR   t   burstt   stats_rolebet_loset   stats_rolebet_wint   menitt   no_wint   no_loset	   total_wint
   total_loset
   no_rolebett   rolebett   waktut   hasil_chancet   cokt   balt   i(    (    R!   t   diceQ   s2   -	
")
"05	H(	`
*	.*	.-
	(TG!!!


0y	

}


xx
�}
"	"

DR=   R>   t   LoginR3   t    33f841d907b2415e92d5c761a348e58ft   Keyt   Accountt   Usernamet   PasswordR!   t   Totps   Balance t   Doget   Balancei
   i   s%   Check Your Username And Your Passwordg     �u@s|   

Maaf Versi Ini Cuma Support Untuk Balance Dibawah 350 Doge
Silahkan Hubungi Author Untuk Full Version
Hub : +6285336117892s
   Target Wins   Lose Targeti ��i ��i ��i ��(8   t   requestsRW   Re   R_   Rc   t   ost   argparset   coloramaR    R   R   R   R   t   initRQ   t   ArgumentParsert   parsert   add_argumentt
   parse_argsRO   t   opent   myfilet   readR>   RX   RR   t   NORMALt   MAGENTAt   GREENRk   t   DIMt   WHITEt	   RESET_ALLRl   RZ   R[   Rm   Rh   Ri   Rj   Rn   t   sessionR   RU   RV   R"   R*   R�   t   getR	   RY   RS   R   R   Rg   R   (    (    (    R!   t   <module>   sZ   T	�	
			�N5$	
(   t   marshalt   loads(    (    (    s   999_.pyt   <module>   s   