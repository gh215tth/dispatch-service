--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3 (Debian 15.3-1.pgdg120+1)
-- Dumped by pg_dump version 15.3 (Debian 15.3-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: processing_status; Type: TYPE; Schema: public; Owner: admin
--

CREATE TYPE public.processing_status AS ENUM (
    'pending',
    'in_progress',
    'completed',
    'archived'
);


ALTER TYPE public.processing_status OWNER TO admin;

--
-- Name: security_level; Type: TYPE; Schema: public; Owner: admin
--

CREATE TYPE public.security_level AS ENUM (
    'public',
    'internal',
    'confidential'
);


ALTER TYPE public.security_level OWNER TO admin;

--
-- Name: urgency_level; Type: TYPE; Schema: public; Owner: admin
--

CREATE TYPE public.urgency_level AS ENUM (
    'normal',
    'urgent',
    'immediate'
);


ALTER TYPE public.urgency_level OWNER TO admin;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO admin;

--
-- Name: dispatch_attachments; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.dispatch_attachments (
    dispatch_id uuid NOT NULL,
    drive_item_id uuid NOT NULL,
    attached_at timestamp without time zone NOT NULL
);


ALTER TABLE public.dispatch_attachments OWNER TO admin;

--
-- Name: dispatch_comments; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.dispatch_comments (
    comment_id uuid NOT NULL,
    dispatch_id uuid NOT NULL,
    author_user_id uuid NOT NULL,
    content text NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


ALTER TABLE public.dispatch_comments OWNER TO admin;

--
-- Name: dispatch_followers; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.dispatch_followers (
    dispatch_id uuid NOT NULL,
    user_id uuid NOT NULL,
    followed_at timestamp without time zone NOT NULL
);


ALTER TABLE public.dispatch_followers OWNER TO admin;

--
-- Name: dispatch_processors; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.dispatch_processors (
    dispatch_id uuid NOT NULL,
    user_id uuid NOT NULL,
    assigned_at timestamp without time zone NOT NULL,
    deadline timestamp without time zone
);


ALTER TABLE public.dispatch_processors OWNER TO admin;

--
-- Name: dispatch_recipients; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.dispatch_recipients (
    dispatch_id uuid NOT NULL,
    user_id uuid NOT NULL,
    notified_at timestamp without time zone
);


ALTER TABLE public.dispatch_recipients OWNER TO admin;

--
-- Name: dispatch_views; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.dispatch_views (
    view_id uuid NOT NULL,
    dispatch_id uuid NOT NULL,
    user_id uuid NOT NULL,
    viewed_at timestamp without time zone NOT NULL
);


ALTER TABLE public.dispatch_views OWNER TO admin;

--
-- Name: dispatches; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.dispatches (
    dispatch_id uuid NOT NULL,
    document_number character varying(100) NOT NULL,
    summary text,
    page_count integer,
    security_level public.security_level NOT NULL,
    urgency_level public.urgency_level NOT NULL,
    processing_status public.processing_status NOT NULL,
    document_type_id uuid NOT NULL,
    issuing_body_id uuid NOT NULL,
    creator_user_id uuid NOT NULL,
    approver_user_id uuid,
    arrival_timestamp timestamp without time zone,
    effective_timestamp timestamp without time zone,
    expiration_timestamp timestamp without time zone,
    approved_at timestamp without time zone,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


ALTER TABLE public.dispatches OWNER TO admin;

--
-- Name: document_types; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.document_types (
    document_type_id uuid NOT NULL,
    name character varying NOT NULL,
    description text
);


ALTER TABLE public.document_types OWNER TO admin;

--
-- Name: issuing_bodies; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.issuing_bodies (
    issuing_body_id uuid NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.issuing_bodies OWNER TO admin;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Data for Name: dispatch_attachments; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.dispatch_attachments (dispatch_id, drive_item_id, attached_at) FROM stdin;
\.


--
-- Data for Name: dispatch_comments; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.dispatch_comments (comment_id, dispatch_id, author_user_id, content, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: dispatch_followers; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.dispatch_followers (dispatch_id, user_id, followed_at) FROM stdin;
\.


--
-- Data for Name: dispatch_processors; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.dispatch_processors (dispatch_id, user_id, assigned_at, deadline) FROM stdin;
\.


--
-- Data for Name: dispatch_recipients; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.dispatch_recipients (dispatch_id, user_id, notified_at) FROM stdin;
\.


--
-- Data for Name: dispatch_views; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.dispatch_views (view_id, dispatch_id, user_id, viewed_at) FROM stdin;
\.


--
-- Data for Name: dispatches; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.dispatches (dispatch_id, document_number, summary, page_count, security_level, urgency_level, processing_status, document_type_id, issuing_body_id, creator_user_id, approver_user_id, arrival_timestamp, effective_timestamp, expiration_timestamp, approved_at, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: document_types; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.document_types (document_type_id, name, description) FROM stdin;
\.


--
-- Data for Name: issuing_bodies; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.issuing_bodies (issuing_body_id, name) FROM stdin;
\.


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: dispatch_attachments dispatch_attachments_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatch_attachments
    ADD CONSTRAINT dispatch_attachments_pkey PRIMARY KEY (dispatch_id, drive_item_id);


--
-- Name: dispatch_comments dispatch_comments_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatch_comments
    ADD CONSTRAINT dispatch_comments_pkey PRIMARY KEY (comment_id);


--
-- Name: dispatch_followers dispatch_followers_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatch_followers
    ADD CONSTRAINT dispatch_followers_pkey PRIMARY KEY (dispatch_id, user_id);


--
-- Name: dispatch_processors dispatch_processors_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatch_processors
    ADD CONSTRAINT dispatch_processors_pkey PRIMARY KEY (dispatch_id, user_id);


--
-- Name: dispatch_recipients dispatch_recipients_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatch_recipients
    ADD CONSTRAINT dispatch_recipients_pkey PRIMARY KEY (dispatch_id, user_id);


--
-- Name: dispatch_views dispatch_views_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatch_views
    ADD CONSTRAINT dispatch_views_pkey PRIMARY KEY (view_id);


--
-- Name: dispatches dispatches_document_number_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatches
    ADD CONSTRAINT dispatches_document_number_key UNIQUE (document_number);


--
-- Name: dispatches dispatches_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatches
    ADD CONSTRAINT dispatches_pkey PRIMARY KEY (dispatch_id);


--
-- Name: document_types document_types_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.document_types
    ADD CONSTRAINT document_types_name_key UNIQUE (name);


--
-- Name: document_types document_types_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.document_types
    ADD CONSTRAINT document_types_pkey PRIMARY KEY (document_type_id);


--
-- Name: issuing_bodies issuing_bodies_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.issuing_bodies
    ADD CONSTRAINT issuing_bodies_name_key UNIQUE (name);


--
-- Name: issuing_bodies issuing_bodies_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.issuing_bodies
    ADD CONSTRAINT issuing_bodies_pkey PRIMARY KEY (issuing_body_id);


--
-- Name: dispatch_attachments dispatch_attachments_dispatch_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatch_attachments
    ADD CONSTRAINT dispatch_attachments_dispatch_id_fkey FOREIGN KEY (dispatch_id) REFERENCES public.dispatches(dispatch_id);


--
-- Name: dispatch_comments dispatch_comments_dispatch_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatch_comments
    ADD CONSTRAINT dispatch_comments_dispatch_id_fkey FOREIGN KEY (dispatch_id) REFERENCES public.dispatches(dispatch_id);


--
-- Name: dispatch_followers dispatch_followers_dispatch_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatch_followers
    ADD CONSTRAINT dispatch_followers_dispatch_id_fkey FOREIGN KEY (dispatch_id) REFERENCES public.dispatches(dispatch_id);


--
-- Name: dispatch_processors dispatch_processors_dispatch_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatch_processors
    ADD CONSTRAINT dispatch_processors_dispatch_id_fkey FOREIGN KEY (dispatch_id) REFERENCES public.dispatches(dispatch_id);


--
-- Name: dispatch_recipients dispatch_recipients_dispatch_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatch_recipients
    ADD CONSTRAINT dispatch_recipients_dispatch_id_fkey FOREIGN KEY (dispatch_id) REFERENCES public.dispatches(dispatch_id);


--
-- Name: dispatch_views dispatch_views_dispatch_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatch_views
    ADD CONSTRAINT dispatch_views_dispatch_id_fkey FOREIGN KEY (dispatch_id) REFERENCES public.dispatches(dispatch_id);


--
-- Name: dispatches dispatches_document_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatches
    ADD CONSTRAINT dispatches_document_type_id_fkey FOREIGN KEY (document_type_id) REFERENCES public.document_types(document_type_id);


--
-- Name: dispatches dispatches_issuing_body_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.dispatches
    ADD CONSTRAINT dispatches_issuing_body_id_fkey FOREIGN KEY (issuing_body_id) REFERENCES public.issuing_bodies(issuing_body_id);


--
-- PostgreSQL database dump complete
--

