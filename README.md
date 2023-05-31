my_fastapi_project/
├── app/ // 包含所有应用代码的目录。
│ ├── api/ // 包含 API 端点的模块。
│ │ ├── **init**.py
│ │ ├── endpoint1.py
│ │ └── ...
│ ├── core/ // 包含核心配置和数据库连接代码的模块。
│ │ ├── **init**.py
│ │ ├── config.py
│ │ └── database.py
│ ├── models/ // 包含数据库模型的模块。
│ │ ├── **init**.py
│ │ ├── model1.py
│ │ └── ...
│ ├── schemas/ // 包含 Pydantic 模式的模块。
│ │ ├── **init**.py
│ │ ├── schema1.py
│ │ └── ...
│ ├── services/ // 包含服务层逻辑的模块，例如数据访问和业务逻辑。
│ │ ├── **init**.py
│ │ ├── service1.py
│ │ └── ...
│ ├── utils/ // 包含实用程序和辅助函数的模块。
│ │ ├── **init**.py
│ │ ├── util1.py
│ │ └── ...
│ ├── **init**.py
│ └── main.py // 应用程序的入口点。
├── tests/ // 包含所有测试代码的目录。
│ ├── **init**.py
│ ├── test_endpoint1.py
│ └── ...
├── .gitignore
├── README.md
├── requirements.txt // 项目所需的 Python 包列表。
└── env // 虚拟环境
