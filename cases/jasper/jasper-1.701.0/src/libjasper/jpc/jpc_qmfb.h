/*
 * Copyright (c) 1999-2000 Image Power, Inc. and the University of
 *   British Columbia.
 * Copyright (c) 2001-2002 Michael David Adams.
 * All rights reserved.
 */

/* __START_OF_JASPER_LICENSE__
 * 
 * JasPer License Version 2.0
 * 
 * Copyright (c) 1999-2000 Image Power, Inc.
 * Copyright (c) 1999-2000 The University of British Columbia
 * Copyright (c) 2001-2003 Michael David Adams
 * 
 * All rights reserved.
 * 
 * Permission is hereby granted, free of charge, to any person (the
 * "User") obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without restriction,
 * including without limitation the rights to use, copy, modify, merge,
 * publish, distribute, and/or sell copies of the Software, and to permit
 * persons to whom the Software is furnished to do so, subject to the
 * following conditions:
 * 
 * 1.  The above copyright notices and this permission notice (which
 * includes the disclaimer below) shall be included in all copies or
 * substantial portions of the Software.
 * 
 * 2.  The name of a copyright holder shall not be used to endorse or
 * promote products derived from the Software without specific prior
 * written permission.
 * 
 * THIS DISCLAIMER OF WARRANTY CONSTITUTES AN ESSENTIAL PART OF THIS
 * LICENSE.  NO USE OF THE SOFTWARE IS AUTHORIZED HEREUNDER EXCEPT UNDER
 * THIS DISCLAIMER.  THE SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS
 * "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
 * BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
 * PARTICULAR PURPOSE AND NONINFRINGEMENT OF THIRD PARTY RIGHTS.  IN NO
 * EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, OR ANY SPECIAL
 * INDIRECT OR CONSEQUENTIAL DAMAGES, OR ANY DAMAGES WHATSOEVER RESULTING
 * FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
 * NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION
 * WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.  NO ASSURANCES ARE
 * PROVIDED BY THE COPYRIGHT HOLDERS THAT THE SOFTWARE DOES NOT INFRINGE
 * THE PATENT OR OTHER INTELLECTUAL PROPERTY RIGHTS OF ANY OTHER ENTITY.
 * EACH COPYRIGHT HOLDER DISCLAIMS ANY LIABILITY TO THE USER FOR CLAIMS
 * BROUGHT BY ANY OTHER ENTITY BASED ON INFRINGEMENT OF INTELLECTUAL
 * PROPERTY RIGHTS OR OTHERWISE.  AS A CONDITION TO EXERCISING THE RIGHTS
 * GRANTED HEREUNDER, EACH USER HEREBY ASSUMES SOLE RESPONSIBILITY TO SECURE
 * ANY OTHER INTELLECTUAL PROPERTY RIGHTS NEEDED, IF ANY.  THE SOFTWARE
 * IS NOT FAULT-TOLERANT AND IS NOT INTENDED FOR USE IN MISSION-CRITICAL
 * SYSTEMS, SUCH AS THOSE USED IN THE OPERATION OF NUCLEAR FACILITIES,
 * AIRCRAFT NAVIGATION OR COMMUNICATION SYSTEMS, AIR TRAFFIC CONTROL
 * SYSTEMS, DIRECT LIFE SUPPORT MACHINES, OR WEAPONS SYSTEMS, IN WHICH
 * THE FAILURE OF THE SOFTWARE OR SYSTEM COULD LEAD DIRECTLY TO DEATH,
 * PERSONAL INJURY, OR SEVERE PHYSICAL OR ENVIRONMENTAL DAMAGE ("HIGH
 * RISK ACTIVITIES").  THE COPYRIGHT HOLDERS SPECIFICALLY DISCLAIM ANY
 * EXPRESS OR IMPLIED WARRANTY OF FITNESS FOR HIGH RISK ACTIVITIES.
 * 
 * __END_OF_JASPER_LICENSE__
 */

/*
 * Quadrature Mirror-Image Filter Bank (QMFB) Routines
 *
 * $Id$
 */

#ifndef JPC_QMFB_H
#define JPC_QMFB_H

/******************************************************************************\
* Includes.
\******************************************************************************/

#include "jasper/jas_seq.h"

/******************************************************************************\
* Constants.
\******************************************************************************/

/* The maximum number of channels for a QMF bank. */
#define	JPC_QMFB1D_MAXCHANS	2

/* Select reversible integer-to-integer mode. */
#define	JPC_QMFB1D_RITIMODE	1

/* Vertical filtering. */
#define	JPC_QMFB1D_VERT	0x10000

/* QMFB IDs. */
#define	JPC_QMFB1D_FT	1	/* 5/3 */
#define	JPC_QMFB1D_NS	2	/* 9/7 */

/******************************************************************************\
* Types.
\******************************************************************************/

/* Forward declaration. */
struct jpc_qmfb1dops_s;

/* Band information. */

typedef struct {

	/* The starting index for the band in the downsampled domain. */
	int start;

	/* The ending index for the band in the downsampled domain. */
	int end;

	/* The location of the start of the band. */
	int locstart;

	/* The location of the end of the band. */
	int locend;

} jpc_qmfb1dband_t;

/* QMF bank */

typedef struct {

	/* The operations for this QMFB. */
	struct jpc_qmfb1dops_s *ops;

} jpc_qmfb1d_t;

/* QMFB operations. */

typedef struct jpc_qmfb1dops_s {

	/* The number of channels in the QMFB. */
	int (*getnumchans)(jpc_qmfb1d_t *qmfb);

	/* Get the analysis filters for this QMFB. */
	int (*getanalfilters)(jpc_qmfb1d_t *qmfb, int len, jas_seq2d_t **filters);

	/* Get the synthesis filters for this QMFB. */
	int (*getsynfilters)(jpc_qmfb1d_t *qmfb, int len, jas_seq2d_t **filters);

	/* Do analysis. */
	void (*analyze)(jpc_qmfb1d_t *qmfb, int flags, jas_seq2d_t *x);

	/* Do synthesis. */
	void (*synthesize)(jpc_qmfb1d_t *qmfb, int flags, jas_seq2d_t *x);

} jpc_qmfb1dops_t;

/******************************************************************************\
* Functions.
\******************************************************************************/

/* Create a QMFB from a QMFB ID. */
jpc_qmfb1d_t *jpc_qmfb1d_make(int qmfbid);

/* Create a copy of a QMFB. */
jpc_qmfb1d_t *jpc_qmfb1d_copy(jpc_qmfb1d_t *qmfb);

/* Destroy a QMFB. */
void jpc_qmfb1d_destroy(jpc_qmfb1d_t *qmfb);

/* Get the number of channels for a QMFB. */
int jpc_qmfb1d_getnumchans(jpc_qmfb1d_t *qmfb);

/* Get the analysis filters for a QMFB. */
int jpc_qmfb1d_getanalfilters(jpc_qmfb1d_t *qmfb, int len,
  jas_seq2d_t **filters);

/* Get the synthesis filters for a QMFB. */
int jpc_qmfb1d_getsynfilters(jpc_qmfb1d_t *qmfb, int len,
  jas_seq2d_t **filters);

/* Get the bands for a QMFB. */
void jpc_qmfb1d_getbands(jpc_qmfb1d_t *qmfb, int flags, uint_fast32_t xstart,
  uint_fast32_t ystart, uint_fast32_t xend, uint_fast32_t yend, int maxbands,
  int *numbandsptr, jpc_qmfb1dband_t *bands);

/* Perform analysis. */
void jpc_qmfb1d_analyze(jpc_qmfb1d_t *qmfb, int flags, jas_seq2d_t *x);

/* Perform synthesis. */
void jpc_qmfb1d_synthesize(jpc_qmfb1d_t *qmfb, int flags, jas_seq2d_t *x);

#endif
