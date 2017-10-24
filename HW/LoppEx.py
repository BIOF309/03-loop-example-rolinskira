{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#real life example of a loop \n",
    "packing = ['kindle ereader', 'headphones', 'toothbrush', 'toothpaste', 'face wash', 'hairbrush', 'sweatshirt', 'tennis shoes', 'boarding pass']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"The total number of items on your packing list is:\")\n",
    "len(packing)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "packing[3] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "for done in packing:\n",
    "    while len(packing) > 0:\n",
    "        print(\"You still have more to pack!\")\n",
    "        print(\"This is how many items you have left to pack:\")\n",
    "        print(len(packing))\n",
    "        print(\"These are the items you have left to pack:\")\n",
    "        print(packing)\n",
    "        print('............')\n",
    "        del(packing[0])\n",
    "    else:\n",
    "        print(\"You're all packed and ready to go... have a great trip!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
