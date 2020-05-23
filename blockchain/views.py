from django.shortcuts import render ,get_object_or_404 , redirect
from main.models import Main
from django.contrib.auth.models import User
from mytransactions.models import Transactiondata
from .models import Blockchains, Thelongestchain
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
import datetime
import hashlib
import json
from django.http import JsonResponse


class Blockchain:

    def __init__(self):
        transdata = Transactiondata.objects.filter().order_by('-id')[0]
        blockchaindatabase = Blockchains.objects.filter().order_by('-id')[1]
        chainvar = Thelongestchain.objects.filter()
        self.name = transdata.sendername
        self.chain = list(chainvar)
        self.create_block(nonce = blockchaindatabase.nonce, previous_hash = str(blockchaindatabase.previoushash))

    def create_block(self, nonce, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'nonce': nonce,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        b = Thelongestchain(longestchain = block)
        b.save()
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_nonce):
        new_nonce = 1
        check_nonce = False
        while check_nonce is False:
            hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_nonce = True
            else:
                new_nonce += 1
        return new_nonce

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_nonce = previous_block['nonce']
            nonce = block['nonce']
            hash_operation = hashlib.sha256(str(nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True


# Creating our Blockchain
blockchain = Blockchain()

# Mining a new block
def mine_block(request):
    if request.method == 'GET':
        thevar = Thelongestchain.objects.filter().order_by('-id')[0]
        theblocknumber = thevar.id
        title = Main.objects.get(pk =1)
        previous_block = blockchain.get_previous_block()
        previous_nonce = previous_block['nonce']
        nonce = blockchain.proof_of_work(previous_nonce)
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(nonce, previous_hash)
        response = {'message': 'Congratulations, you just mined a block!',
                    'index': block['index'],
                    'timestamp': block['timestamp'],
                    'nonce': block['nonce'],
                    'previous_hash': block['previous_hash']}
        message = "'Message': 'Congratulations, Your Transaction is appended in our block!' "
        index= block['index']
        previous_hash = block['previous_hash']
        b = Blockchains(index =block['index'],nonce =block['nonce'],timestamp =  block['timestamp'],previoushash =block['previous_hash'],sendername =request.user ,thechain = response)
        b.save()
    return render(request,'blockchain/index.html',{'message':message,'theblocknumber':theblocknumber,'previous_hash':previous_hash,'title':title})

# Getting the full Blockchain
def get_chain(request):
    if request.method == 'GET':
        response = {'chain': str(blockchain.chain),
                    'length': len(blockchain.chain)}
    return JsonResponse(response)

# Checking if the Blockchain is valid
def is_valid(request):
    if request.method == 'GET':
        is_valid = blockchain.is_chain_valid(blockchain.chain)
        if is_valid:
            response = {'message': 'All good. The Blockchain is valid.'}
        else:
            response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
    return JsonResponse(response)


def testing(request):
    thevar = Thelongestchain.objects.filter().order_by('-id')[0]
    thevari = Thelongestchain.objects.filter()
    transdata = Transactiondata.objects.filter().order_by('-id')[0]
    blockchaindatabase = Blockchains.objects.filter().order_by('-id')[0]
    print(thevar.id)
    print(blockchaindatabase.index,blockchaindatabase.nonce,blockchaindatabase.previoushash)
    print(transdata.sendername)
    print(list(thevari))


    return HttpResponse("test")



