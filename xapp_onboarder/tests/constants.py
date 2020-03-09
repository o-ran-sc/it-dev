################################################################################
#   Copyright (c) 2020 AT&T Intellectual Property.                             #
#                                                                              #
#   Licensed under the Apache License, Version 2.0 (the "License");            #
#   you may not use this file except in compliance with the License.           #
#   You may obtain a copy of the License at                                    #
#                                                                              #
#       http://www.apache.org/licenses/LICENSE-2.0                             #
#                                                                              #
#   Unless required by applicable law or agreed to in writing, software        #
#   distributed under the License is distributed on an "AS IS" BASIS,          #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
#   See the License for the specific language governing permissions and        #
#   limitations under the License.                                             #
################################################################################

schema_file = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "http://example.com/root.json",
    "type": "object",
    "title": "The Root Schema",
    "required": [
        "local",
        "logger",
        "rmr",
        "db",
        "controls",
        "metrics"
    ],
    "properties": {
        "local": {
            "$id": "#/properties/local",
            "type": "object",
            "title": "The Local Schema",
            "required": [
                "host"
            ],
            "properties": {
                "host": {
                    "$id": "#/properties/local/properties/host",
                    "type": "string",
                    "title": "The Host Schema",
                    "default": "",
                    "examples": [
                        ":8080"
                    ],
                    "pattern": "^(.*)$"
                }
            }
        },
        "logger": {
            "$id": "#/properties/logger",
            "type": "object",
            "title": "The Logger Schema",
            "required": [
                "level"
            ],
            "properties": {
                "level": {
                    "$id": "#/properties/logger/properties/level",
                    "type": "integer",
                    "title": "The Level Schema",
                    "default": 0,
                    "examples": [
                        3
                    ]
                }
            }
        },
        "rmr": {
            "$id": "#/properties/rmr",
            "type": "object",
            "title": "The Rmr Schema",
            "required": [
                "protPort",
                "maxSize",
                "numWorkers",
                "rxMessages",
                "txMessages"
            ],
            "properties": {
                "protPort": {
                    "$id": "#/properties/rmr/properties/protPort",
                    "type": "string",
                    "title": "The Protport Schema",
                    "default": "",
                    "examples": [
                        "tcp:4560"
                    ],
                    "pattern": "^(.*)$"
                },
                "maxSize": {
                    "$id": "#/properties/rmr/properties/maxSize",
                    "type": "integer",
                    "title": "The Maxsize Schema",
                    "default": 0,
                    "examples": [
                        2072
                    ]
                },
                "numWorkers": {
                    "$id": "#/properties/rmr/properties/numWorkers",
                    "type": "integer",
                    "title": "The Numworkers Schema",
                    "default": 0,
                    "examples": [
                        1
                    ]
                },
                "rxMessages": {
                    "$id": "#/properties/rmr/properties/rxMessages",
                    "type": "array",
                    "title": "The Rxmessages Schema",
                    "items": {
                        "$id": "#/properties/rmr/properties/rxMessages/items",
                        "type": "string",
                        "title": "The Items Schema",
                        "default": "",
                        "examples": [
                            "RIC_SUB_RESP",
                            "RIC_SUB_FAILURE",
                            "RIC_SUB_DEL_RESP",
                            "RIC_SUB_DEL_FAILURE",
                            "RIC_INDICATION"
                        ],
                        "pattern": "^(.*)$"
                    }
                },
                "txMessages": {
                    "$id": "#/properties/rmr/properties/txMessages",
                    "type": "array",
                    "title": "The Txmessages Schema",
                    "items": {
                        "$id": "#/properties/rmr/properties/txMessages/items",
                        "type": "string",
                        "title": "The Items Schema",
                        "default": "",
                        "examples": [
                            "RIC_SUB_REQ",
                            "RIC_SUB_DEL_REQ",
                            "RIC_SGNB_ADDITION_REQ",
                            "RIC_SGNB_ADDITION_ACK",
                            "RIC_SGNB_ADDITION_REJECT",
                            "RIC_SGNB_MOD_REQUEST",
                            "RIC_SGNB_MOD_REQUEST_ACK",
                            "RIC_SGNB_MOD_REQUEST_REJECT",
                            "RIC_SGNB_MOD_REQUIRED",
                            "RIC_SGNB_MOD_CONFIRM",
                            "RIC_SGNB_MOD_REFUSE",
                            "RIC_SGNB_RECONF_COMPLETE",
                            "RIC_SGNB_RELEASE_REQUEST",
                            "RIC_SGNB_RELEASE_CONFIRM",
                            "RIC_SGNB_RELEASE_REQUIRED",
                            "RIC_SGNB_RELEASE_REQUEST_ACK",
                            "RIC_SECONDARY_RAT_DATA_USAGE_REPORT",
                            "RIC_SN_STATUS_TRANSFER",
                            "RIC_RRC_TRANSFER",
                            "RIC_UE_CONTEXT_RELEASE"
                        ],
                        "pattern": "^(.*)$"
                    }
                }
            }
        },
        "db": {
            "$id": "#/properties/db",
            "type": "object",
            "title": "The Db Schema",
            "required": [
                "host",
                "port",
                "namespaces"
            ],
            "properties": {
                "host": {
                    "$id": "#/properties/db/properties/host",
                    "type": "string",
                    "title": "The Host Schema",
                    "default": "",
                    "examples": [
                        "localhost"
                    ],
                    "pattern": "^(.*)$"
                },
                "port": {
                    "$id": "#/properties/db/properties/port",
                    "type": "integer",
                    "title": "The Port Schema",
                    "default": 0,
                    "examples": [
                        6379
                    ]
                },
                "namespaces": {
                    "$id": "#/properties/db/properties/namespaces",
                    "type": "array",
                    "title": "The Namespaces Schema",
                    "items": {
                        "$id": "#/properties/db/properties/namespaces/items",
                        "type": "string",
                        "title": "The Items Schema",
                        "default": "",
                        "examples": [
                            "sdl",
                            "rnib"
                        ],
                        "pattern": "^(.*)$"
                    }
                }
            }
        },
        "controls": {
            "$id": "#/properties/controls",
            "type": "object",
            "title": "The Controls Schema",
            "required": [
                "active",
                "requestorId",
                "ranFunctionId",
                "ricActionId",
                "interfaceId"
            ],
            "properties": {
                "active": {
                    "$id": "#/properties/controls/properties/active",
                    "type": "boolean",
                    "title": "The Active Schema",
                    "default": False,
                    "examples": [
                        True
                    ]
                },
                "requestorId": {
                    "$id": "#/properties/controls/properties/requestorId",
                    "type": "integer",
                    "title": "The Requestorid Schema",
                    "default": 0,
                    "examples": [
                        66
                    ]
                },
                "ranFunctionId": {
                    "$id": "#/properties/controls/properties/ranFunctionId",
                    "type": "integer",
                    "title": "The Ranfunctionid Schema",
                    "default": 0,
                    "examples": [
                        1
                    ]
                },
                "ricActionId": {
                    "$id": "#/properties/controls/properties/ricActionId",
                    "type": "integer",
                    "title": "The Ricactionid Schema",
                    "default": 0,
                    "examples": [
                        0
                    ]
                },
                "interfaceId": {
                    "$id": "#/properties/controls/properties/interfaceId",
                    "type": "object",
                    "title": "The Interfaceid Schema",
                    "required": [
                        "globalENBId"
                    ],
                    "properties": {
                        "globalENBId": {
                            "$id": "#/properties/controls/properties/interfaceId/properties/globalENBId",
                            "type": "object",
                            "title": "The Globalenbid Schema",
                            "required": [
                                "plmnId",
                                "eNBId"
                            ],
                            "properties": {
                                "plmnId": {
                                    "$id": "#/properties/controls/properties/interfaceId/properties/globalENBId/properties/plmnId",
                                    "type": "string",
                                    "title": "The Plmnid Schema",
                                    "default": "",
                                    "examples": [
                                        "310150"
                                    ],
                                    "pattern": "^(.*)$"
                                },
                                "eNBId": {
                                    "$id": "#/properties/controls/properties/interfaceId/properties/globalENBId/properties/eNBId",
                                    "type": "integer",
                                    "title": "The Enbid Schema",
                                    "default": 0,
                                    "examples": [
                                        202251
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        },
        "metrics": {
            "$id": "#/properties/metrics",
            "type": "array",
            "title": "The Metrics Schema",
            "items": {
                "$id": "#/properties/metrics/items",
                "type": "object",
                "title": "The Items Schema",
                "required": [
                    "objectName",
                    "objectInstance",
                    "name",
                    "type",
                    "description"
                ],
                "properties": {
                    "objectName": {
                        "$id": "#/properties/metrics/items/properties/objectName",
                        "type": "string",
                        "title": "The Objectname Schema",
                        "default": "",
                        "examples": [
                            "UEEventStreamingCounters"
                        ],
                        "pattern": "^(.*)$"
                    },
                    "objectInstance": {
                        "$id": "#/properties/metrics/items/properties/objectInstance",
                        "type": "string",
                        "title": "The Objectinstance Schema",
                        "default": "",
                        "examples": [
                            "SgNBAdditionRequest"
                        ],
                        "pattern": "^(.*)$"
                    },
                    "name": {
                        "$id": "#/properties/metrics/items/properties/name",
                        "type": "string",
                        "title": "The Name Schema",
                        "default": "",
                        "examples": [
                            "SgNBAdditionRequest"
                        ],
                        "pattern": "^(.*)$"
                    },
                    "type": {
                        "$id": "#/properties/metrics/items/properties/type",
                        "type": "string",
                        "title": "The Type Schema",
                        "default": "",
                        "examples": [
                            "counter"
                        ],
                        "pattern": "^(.*)$"
                    },
                    "description": {
                        "$id": "#/properties/metrics/items/properties/description",
                        "type": "string",
                        "title": "The Description Schema",
                        "default": "",
                        "examples": [
                            "The total number of SG addition request events processed"
                        ],
                        "pattern": "^(.*)$"
                    }
                }
            }
        }
    }
}

config_file = {
    "chart_name": "test_xapp",
    "version": "1.0.0",
    "containers": [{
        "name": "test1",
        "image": {
            "registry": "test_repo",
            "name": "test_name",
            "tag": "test_tag"
        },
        "command": "test command"
    },
        {
            "name": "test2",
            "image": {
                "registry": "test2_repo",
                "name": "test2_name",
                "tag": "test2:_tag"
            },
            "command": "test2 command"
        }],
    "local": {
        "host": ":8080"
    },
    "logger": {
        "level": 3
    },
    "db": {
        "host": "localhost",
        "port": 6379,
        "namespaces": ["sdl", "rnib"]
    },
    "controls": {
        "active": True,
        "requestorId": 66,
        "ranFunctionId": 1,
        "ricActionId": 0,
        "interfaceId": {
            "globalENBId": {
                "plmnId": "310150",
                "eNBId": 202251
            }
        }
    },
    "rmr": {
        "protPort": "tcp:4560",
        "maxSize": 10000,
        "numWorkers": 1,
        "rxMessages": [
            "RIC_SUB_RESP",
            "RIC_SUB_FAILURE",
            "RIC_SUB_DEL_RESP",
            "RIC_SUB_DEL_FAILURE",
            "RIC_INDICATION"
        ],
        "txMessages": [
            "RIC_SUB_REQ",
            "RIC_SUB_DEL_REQ",
            "RIC_SGNB_ADDITION_REQ",
            "RIC_SGNB_ADDITION_ACK",
            "RIC_SGNB_ADDITION_REJECT",
            "RIC_SGNB_MOD_REQUEST",
            "RIC_SGNB_MOD_REQUEST_ACK",
            "RIC_SGNB_MOD_REQUEST_REJECT",
            "RIC_SGNB_MOD_REQUIRED",
            "RIC_SGNB_MOD_CONFIRM",
            "RIC_SGNB_MOD_REFUSE",
            "RIC_SGNB_RELEASE_REQUEST",
            "RIC_SGNB_RELEASE_CONFIRM",
            "RIC_SGNB_RELEASE_REQUIRED",
            "RIC_SGNB_RELEASE_REQUEST_ACK",
            "RIC_SGNB_RECONF_COMPLETE",
            "RIC_UE_CONTEXT_RELEASE",
            "RIC_RRC_TRANSFER",
            "RIC_SECONDARY_RAT_DATA_USAGE_REPORT",
            "RIC_SN_STATUS_TRANSFER"
        ]
    },
    "metrics": [
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBAdditionRequest",
            "name": "SgNBAdditionRequest",
            "type": "counter",
            "description": "The total number of SG addition request events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBAdditionRequestAcknowledge",
            "name": "SgNBAdditionRequestAcknowledge",
            "type": "counter",
            "description": "The total number of SG addition request acknowledge events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBAdditionRequestReject",
            "name": "SgNBAdditionRequestReject",
            "type": "counter",
            "description": "The total number of SG addition request reject events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBModificationRequest",
            "name": "SgNBModificationRequest",
            "type": "counter",
            "description": "The total number of SG modification request events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBModificationRequestAcknowledge",
            "name": "SgNBModificationRequestAcknowledge",
            "type": "counter",
            "description": "The total number of SG modification request acknowledge events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBModificationRequestReject",
            "name": "SgNBModificationRequestReject",
            "type": "counter",
            "description": "The total number of SG modification request reject events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBModificationRequired",
            "name": "SgNBModificationRequired",
            "type": "counter",
            "description": "The total number of SG modification required events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBModificationConfirm",
            "name": "SgNBModificationConfirm",
            "type": "counter",
            "description": "The total number of SG modification confirm events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBModificationRefuse",
            "name": "SgNBModificationRefuse",
            "type": "counter",
            "description": "The total number of SG modification refuse events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBReleaseRequest",
            "name": "SgNBReleaseRequest",
            "type": "counter",
            "description": "The total number of SG release request events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBReleaseRequestAcknowledge",
            "name": "SgNBReleaseRequestAcknowledge",
            "type": "counter",
            "description": "The total number of SG release request acknowledge events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBReleaseRequestReject",
            "name": "SgNBReleaseRequestReject",
            "type": "counter",
            "description": "The total number of SG release request reject events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBReleaseRequired",
            "name": "SgNBReleaseRequired",
            "type": "counter",
            "description": "The total number of SG release required events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBReleasenConfirm",
            "name": "SgNBReleasenConfirm",
            "type": "counter",
            "description": "The total number of SG release confirm events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SgNBReconfigurationComplete",
            "name": "SgNBReconfigurationComplete",
            "type": "counter",
            "description": "The total number of SG reconfiguration complete events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "UEContextRelease",
            "name": "UEContextRelease",
            "type": "counter",
            "description": "The total number of SG UE context release events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "RRCTransfer",
            "name": "RRCTransfer",
            "type": "counter",
            "description": "The total number of SG RRC transfers events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SNStatusTransfer",
            "name": "SNStatusTransfer",
            "type": "counter",
            "description": "The total number of SG SN status transfers events processed"
        },
        {
            "objectName": "UEEventStreamingCounters",
            "objectInstance": "SecondaryRATDataUsageReport",
            "name": "SecondaryRATDataUsageReport",
            "type": "counter",
            "description": "The total number of SG secondary RAT data usage reports events processed"
        },
        {
            "objectName": "RMRCounters",
            "objectInstance": "Transmitted",
            "name": "Transmitted",
            "type": "counter",
            "description": "The total number of RMR messages transmited"
        },
        {
            "objectName": "RMRCounters",
            "objectInstance": "Received",
            "name": "Received",
            "type": "counter",
            "description": "The total number of RMR messages received"
        },
        {
            "objectName": "RMRCounters",
            "objectInstance": "TransmitError",
            "name": "TransmitError",
            "type": "counter",
            "description": "The total number of RMR messages transmission errors"
        },
        {
            "objectName": "RMRCounters",
            "objectInstance": "ReceiveError",
            "name": "ReceiveError",
            "type": "counter",
            "description": "The total number of RMR messages receive errors"
        },
        {
            "objectName": "SDLounters",
            "objectInstance": "Stored",
            "name": "Stored",
            "type": "counter",
            "description": "The total number of stored SDL transactions"
        },
        {
            "objectName": "SDLounters",
            "objectInstance": "StoreError",
            "name": "StoreError",
            "type": "counter",
            "description": "The total number of SDL store errors"
        }
    ]
}

mock_json_body_url = {
    'config-file.json_url': 'http://0.0.0.0:8080/config-file.json',
    'schema.json_url': 'http://0.0.0.0:8080/schema.json'
}

mock_json_body = {
    "config-file.json": config_file,
    "schema.json": schema_file
}

helm_repo_index_response={'apiVersion': 'v1',
                'entries':{
                    'test_xapp':[{
                        'apiVersion': 'v1',
                        'appVersion': '1.0',
                        'created': '2020-03-12T19:10:17.178396719Z',
                        'description': 'test xApp Helm Chart',
                        'digest': 'd77dfb3f008e5174e90d79bfe982ef85b5dc5930141f6a1bd9995b2fa35',
                        'name': 'test_xapp',
                        'urls':['charts/test-1.0.0.tgz'],
                        'version': '1.0.0'
                    }]
                },
                'generated': '2020-03-16T16:54:44Z',
                'serverInfo':{}
                }