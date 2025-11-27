CREATE TABLE [dbo].[tblProducts](
	[ProductID] [int] IDENTITY(1,1) NOT NULL PRIMARY KEY,
	[Name] [nvarchar](50) NOT NULL,
	[Price] [money] NULL,
);
