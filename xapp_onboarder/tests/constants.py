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
    "definitions": {
    },
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "http://example.com/root.json",
    "type": "object",
    "title": "The Root Schema",
    "required": [
        "xapp_name",
        "version",
        "containers"
    ],
    "properties": {
        "xapp_name": {
            "$id": "#/properties/xapp_name",
            "type": "string",
            "title": "The xApp Name",
            "default": "xapp",
            "examples": [
                "example_xapp"
            ]
        },
        "version": {
            "$id": "#/properties/version",
            "type": "string",
            "title": "The xApp version",
            "default": "1.0.0",
            "examples": [
                "1.0.0"
            ],
            "pattern": "^(0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?$"
        },
        "containers": {
            "$id": "#/properties/containers",
            "type": "array",
            "title": "The Container Schema",
            "items": {
                "$id": "#/properties/containers/items",
                "type": "object",
                "title": "The Container Items Schema",
                "required": [
                    "name",
                    "image"
                ],
                "properties": {
                    "name": {
                        "$id": "#/properties/containers/items/properties/name",
                        "type": "string",
                        "title": "The xApp Container Name",
                        "default": "xapp",
                        "examples": [
                            "xapp"
                        ]
                    },
                    "image": {
                        "$id": "#/properties/containers/items/properties/image",
                        "type": "object",
                        "title": "The Container Image",
                        "required": [
                            "registry",
                            "name",
                            "tag"
                        ],
                        "properties": {
                            "registry": {
                                "$id": "#/properties/containers/items/properties/image/properties/registry",
                                "type": "string",
                                "title": "The xApp Image Registry",
                                "default": "nexus3.o-ran-sc.org:10002",
                                "examples": [
                                    "nexus3.o-ran-sc.org:10002"
                                ],
                                "pattern": "^[A-Za-z0-9\\.-]{1,}\\.[A-Za-z]{1,}(?:\\:\\d+)?$"
                            },
                            "name": {
                                "$id": "#/properties/containers/items/properties/image/properties/name",
                                "type": "string",
                                "title": "The xApp Image Name",
                                "default": "xapp",
                                "examples": [
                                    "xapp"
                                ]
                            },
                            "tag": {
                                "$id": "#/properties/containers/items/properties/image/properties/tag",
                                "type": "string",
                                "title": "The xApp Image Tag",
                                "default": "latest",
                                "examples": [
                                    "latest"
                                ]
                            }
                        }
                    },
                    "command": {
                        "$id": "#/properties/containers/items/properties/command",
                        "type": "string",
                        "title": "Command To Run The xApp Container",
                        "default": "command",
                        "examples": [
                            "command"
                        ]
                    }
                }
            }
        },
        "livenessProbe": {
            "$id": "#/properties/livenessprobe",
            "type": "object",
            "title": "The Liveness Probe Definition",
            "properties": {
                "exec": {
                    "$id": "#/properties/livenessprobe/exec",
                    "type": "object",
                    "title": "Script of Liveness Probe",
                    "properties": {
                        "command": {
                            "$id": "#/properties/livenessprobe/exec/command",
                            "type": "array",
                            "items": [
                                {
                                    "$id": "#/properties/livenessprobe/exec/command/item",
                                    "type": "string",
                                    "title": "The Command Item",
                                    "default": "/bin/sh",
                                    "examples": [
                                        "/bin/sh"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "command"
                    ]
                },
                "httpGet": {
                    "$id": "#/properties/livenessprobe/httpget",
                    "type": "object",
                    "title": "Http of Liveness Probe",
                    "properties": {
                        "path": {
                            "$id": "#/properties/livenessprobe/httpget/path",
                            "type": "string",
                            "title": "The Path of Http Liveness Probe",
                            "default": "/health",
                            "examples": [
                                "/health"
                            ]
                        },
                        "port": {
                            "$id": "#/properties/livenessprobe/httpget/port",
                            "type": "integer",
                            "title": "The Port of Http Liveness Probe",
                            "default": 80,
                            "examples": [
                                80
                            ]
                        }
                    },
                    "required": [
                        "path",
                        "port"
                    ]
                },
                "initialDelaySeconds": {
                    "$id": "#/properties/livenessprobe/initialdelayseconds",
                    "type": "integer",
                    "title": "Initial Delay of Liveness Probe",
                    "default": 5,
                    "examples": [
                        5
                    ]
                },
                "periodSeconds": {
                    "$id": "#/properties/livenessprobe/periodseconds",
                    "type": "integer",
                    "title": "Period of Liveness Probe",
                    "default": 15,
                    "examples": [
                        15
                    ]
                }
            },
            "oneOf": [
                {
                    "$id": "#/properties/livenessprobe/oneof/exec",
                    "required": ["exec", "initialDelaySeconds", "periodSeconds"]
                },
                {
                    "$id": "#/properties/livenessprobe/oneof/httpget",
                    "required": ["httpGet", "initialDelaySeconds", "periodSeconds"]
                }
            ]
        },
        "readinessProbe": {
            "$id": "#/properties/readinessprobe",
            "type": "object",
            "title": "The Readiness Probe Definition",
            "properties": {
                "exec": {
                    "$id": "#/properties/readinessprobe/exec",
                    "type": "object",
                    "title": "Script of Readiness Probe",
                    "properties": {
                        "command": {
                            "$id": "#/properties/readinessprobe/exec/command",
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                }
                            ]
                        }
                    },
                    "required": [
                        "command"
                    ]
                },
                "httpGet": {
                    "$id": "#/properties/readinessprobe/httpget",
                    "type": "object",
                    "title": "Http of Readiness Probe",
                    "properties": {
                        "path": {
                            "$id": "#/properties/readinessprobe/httpget/path",
                            "type": "string",
                            "title": "The Path of Http Readiness Probe",
                            "default": "/health",
                            "examples": [
                                "/health"
                            ]
                        },
                        "port": {
                            "$id": "#/properties/readinessprobe/httpget/port",
                            "type": "integer",
                            "title": "The Port of Http Readiness Probe",
                            "default": 80,
                            "examples": [
                                80
                            ]
                        }
                    },
                    "required": [
                        "path",
                        "port"
                    ]
                },
                "initialDelaySeconds": {
                    "$id": "#/properties/readinessprobe/initialdelayseconds",
                    "type": "integer",
                    "title": "Initial Delay of Readiness Probe",
                    "default": 5,
                    "examples": [
                        5
                    ]
                },
                "periodSeconds": {
                    "$id": "#/properties/readinessprobe/periodseconds",
                    "type": "integer",
                    "title": "Period of Readiness Probe",
                    "default": 15,
                    "examples": [
                        15
                    ]
                }
            },
            "oneOf": [
                {
                    "$id": "#/properties/readinessprobe/oneof/exec",
                    "required": ["exec", "initialDelaySeconds", "periodSeconds"]
                },
                {
                    "$id": "#/properties/readinessprobe/oneof/httpget",
                    "required": ["httpGet", "initialDelaySeconds", "periodSeconds"]
                }
            ]
        },
        "messaging": {
            "type": "object",
            "$id": "#/properties/messaging",
            "title": "The Messaging Schema",
            "properties": {
                "ports": {
                    "$id": "#/properties/messaging/ports",
                    "type": "array",
                    "title": "The Ports for Messaging",
                    "items": {
                        "$id": "#/properties/messaging/ports/items",
                        "type": "object",
                        "title": "The Item of Port",
                        "required": [
                            "name",
                            "container",
                            "port"
                        ],
                        "properties": {
                            "name": {
                                "$id": "#/properties/messaging/ports/items/name",
                                "type": "string",
                                "title": "The Name of the Port",
                                "default": "App",
                                "examples": [
                                    "App"
                                ]
                            },
                            "container": {
                                "$id": "#/properties/messaging/ports/items/container",
                                "type": "string",
                                "title": "The Container of the Port",
                                "default": "xapp",
                                "examples": [
                                    "xapp"
                                ]
                            },
                            "port": {
                                "$id": "#/properties/messaging/ports/items/port",
                                "type": "integer",
                                "title": "The Port Number",
                                "default": 8080,
                                "examples": [
                                    8080
                                ]
                            }
                        }
                    }
                },
                "maxSize": {
                    "$id": "#/properties/messaging/maxsize",
                    "type": "integer",
                    "title": "The Maximum RMR Buffer Size",
                    "default": 2072,
                    "examples": [
                        2072
                    ]
                },
                "numWorkers": {
                    "$id": "#/properties/messaging/numworkers",
                    "type": "integer",
                    "title": "The Number of RMR workers",
                    "default": 1,
                    "examples": [
                        1
                    ]
                },
                "txMessages": {
                    "$id": "#/properties/messaging/txmessages",
                    "type": "array",
                    "title": "The txMessage Types",
                    "items": {
                        "$id": "#/properties/messaging/txmessages/item",
                        "type": "string",
                        "title": "The txMessage Types Item",
                        "default": "RIC_SUB",
                        "examples": [
                            "RIC_SUB"
                        ]
                    }
                },
                "rxMessages": {
                    "$id": "#/properties/messaging/rxmessages",
                    "type": "array",
                    "title": "The rxMessage Types",
                    "items": {
                        "$id": "#/properties/messaging/rxmessages/item",
                        "type": "string",
                        "title": "The rxMessage Types Item",
                        "default": "RIC_SUB",
                        "examples": [
                            "RIC_SUB"
                        ]
                    }
                },
                "policies": {
                    "$id": "#/properties/messaging/policies",
                    "type": "array",
                    "title": "The Policies Types",
                    "items": {
                        "$id": "#/properties/messaging/policies/item",
                        "type": "integer",
                        "title": "The Policy Types Item",
                        "default": 1,
                        "examples": [
                            1
                        ]
                    }
                }
            },
            "required": [
                "ports",
                "maxSize",
                "numWorkers",
                "txMessages",
                "rxMessages",
                "policies"
            ]

        },
        "controls": {
            "type": "object",
            "$id": "#/properties/controls",
            "title": "The Controls Schema"
        },
        "metrics": {
            "type": "array",
            "$id": "#/properties/metrics",
            "title": "The Metrics Schema",
            "items": {
                "$id": "#/properties/metrics/items",
                "type": "object",
                "title": "The Metrics Items Schema",
                "required": [
                    "objectName",
                    "objectInstance",
                    "name",
                    "type",
                    "description"
                ],
                "properties": {
                    "objectName": {
                        "$id": "#/properties/metrics/items/objectname",
                        "type": "string",
                        "title": "The Object Name"
                    },
                    "objectInstance": {
                        "$id": "#/properties/metrics/items/objectinstance",
                        "type": "string",
                        "title": "The Object Instance"
                    },
                    "name": {
                        "$id": "#/properties/metrics/items/name",
                        "type": "string",
                        "title": "The Object Name"
                    },
                    "type": {
                        "$id": "#/properties/metrics/items/type",
                        "type": "string",
                        "title": "The Object Type"
                    },
                    "description": {
                        "$id": "#/properties/metrics/items/description",
                        "type": "string",
                        "title": "The Object Description"
                    }
                }
            }
        }
    }
}

config_file = {
    "xapp_name": "test_xapp",
    "version": "1.0.0",
    "containers": [
        {
            "name": "mcxapp",
            "image": {
                "registry": "nexus3.o-ran-sc.org:10002",
                "name": "o-ran-sc/ric-app-mc",
                "tag": "1.0.2"
            },
            "command": "/playpen/bin/container_start.sh"
        }
    ],
    "livenessProbe": {
        "exec": {
            "command": ["/usr/local/bin/health_ck"]
        },
        "initialDelaySeconds": 5,
        "periodSeconds": 15
    },
    "readinessProbe": {
        "httpGet": {
            "path": "ric/v1/health/alive",
            "port": 8080
        },
        "initialDelaySeconds": 5,
        "periodSeconds": 15
    },
    "messaging": {
        "ports": [
            {
                "name": "http",
                "container": "mcxapp",
                "port": 8080,
                "description": "http service"
            },
            {
                "name": "rmr_data",
                "container": "mcxapp",
                "port": 4560,
                "description": "rmr data port for mcxapp"
            },
            {
                "name": "rmr_route",
                "container": "mcxapp",
                "port": 4561,
                "description": "rmr route port for mcxapp"
            }
        ],
        "maxSize": 2072,
        "numWorkers": 1,
        "txMessages": [
            "RIC_SUB_REQ",
            "RIC_SUB_DEL_REQ"
        ],
        "rxMessages": [
            "RIC_SUB_RESP",
            "RIC_SUB_FAILURE",
            "RIC_SUB_DEL_RESP",
            "RIC_INDICATION"
        ],
        "policies": [1, 2]
    },
    "controls": {
        "active": "true",
        "interfaceId": {
            "globalENBId": {
                "plmnId": 123456,
                "eNBId": 5678
            }
        },
        "ves_collector_address": "xapp-sandbox2.research.att.com:8888",
        "measurement_interval": 10000,
        "simulator_mode": "true",
        "debug_mode": "true",
        "local": {
            "host": ":8080"
        },
        "logger": {
            "level": 3
        }
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

helm_repo_index_response = {'apiVersion': 'v1',
                            'entries': {
                                'test_xapp': [{
                                    'apiVersion': 'v1',
                                    'appVersion': '1.0',
                                    'created': '2020-03-12T19:10:17.178396719Z',
                                    'description': 'test xApp Helm Chart',
                                    'digest': 'd77dfb3f008e5174e90d79bfe982ef85b5dc5930141f6a1bd9995b2fa35',
                                    'name': 'test_xapp',
                                    'urls': ['charts/test-1.0.0.tgz'],
                                    'version': '1.0.0'
                                }]
                            },
                            'generated': '2020-03-16T16:54:44Z',
                            'serverInfo': {}
                            }
