# VMware vSphere Python SDK Community Samples Addons
# Copyright (c) 2014 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module implements simple helper functions for python samples working with
virtual machine objects
"""
__author__ = "VMware, Inc."


def print_vm_info(vm, depth=1, max_depth=10):
    """
    Print information for a particular virtual machine or recurse into a
    folder with depth protection
    """

    # if this is a group it will have children. if it does, recurse into them
    # and then return
    if hasattr(vm, 'childEntity'):
        if depth > max_depth:
            return
        vmList = vm.childEntity
        for c in vmList:
            print_vm_info(c, depth + 1)
        return
    returnDict = {'name':'','path':'','guest':'','annotation':'','state':'','ip':'','question':'','numVirtualDisks':'','numEthernetCards':'','template':'','memorySizeMB':''}
    summary = vm.summary
    #print "Name       : ", summary.config.name
    #print "Path       : ", summary.config.vmPathName
    #print "Guest      : ", summary.config.guestFullName
    returnDict['name'] = summary.config.name
    returnDict['path'] = summary.config.vmPathName
    returnDict['guest'] = summary.config.guestFullName

    try:
        returnDict['numVirtualDisks'] = summary.config.numVirtualDisks
    except:
        pass
    try:
        returnDict['numEthernetCards'] = summary.config.numEthernetCards
    except:
        pass
    try:
        returnDict['template'] = summary.config.template
    except:
        pass
    try:
        returnDict['memorySizeMB'] = summary.config.memorySizeMB
    except:
        pass

    annotation = summary.config.annotation
    if annotation:
        #print "Annotation : ", annotation
        returnDict['annotation'] = annotation
    #print "State      : ", summary.runtime.powerState
    returnDict['state'] = summary.runtime.powerState
    if summary.guest is not None:
        ip = summary.guest.ipAddress
        if ip:
            #print "IP         : ", ip
            returnDict['ip'] = ip
    if summary.runtime.question is not None:
        #print "Question  : ", summary.runtime.question.text
        returnDict['question'] = summary.runtime.question.text
    #print ""
    return(returnDict)
