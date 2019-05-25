#!/usr/bin/env checkio --domain=js run friendly-number

// https://js.checkio.org/mission/friendly-number/

// 
// END_DESC

"use strict";

function friendlyNumber(number, options){
    if (!options) {
        options = {};
    }
    if (!options.base) {
        options.base = 1000;
    }
    if (!options.decimals) {
        options.decimals = 0;
    }
    if (!options.suffix) {
        options.suffix = '';
    }
    if (!options.powers) {
        options.powers = ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'];
    }
    return String(number);
}

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(friendlyNumber(102), '102', "102");
    assert.equal(friendlyNumber(10240), '10k', "10k");
    assert.equal(friendlyNumber(12341234, {decimals: 1}), '12.3M', "12.3M");
    assert.equal(friendlyNumber(12461, {decimals: 1}), '12.5k', "12.5k");
    assert.equal(friendlyNumber(1024000000, {base: 1024, suffix: 'iB'}), '976MiB', "976MiB");
    console.log("Tests and earn cool rewards!");
}